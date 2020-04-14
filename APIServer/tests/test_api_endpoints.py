"""
"""
import json
import random
import string
from unittest import TestCase, main, skip

from flask_restplus import Resource

from APIServer.api_endpoints import Props, ModelMenu, RunModel
from APIServer.api_endpoints import Props, ModelMenu, RunModel
from APIServer.api_endpoints import app, HelloWorld, Endpoints, Models
from APIServer.api_endpoints import indra_dir
from APIServer.api_utils import err_return
from APIServer.models_api import load_models, MODEL_FILE

menu = [{"val": 0, "func": "run", "question": "Run for N periods"},
        {"val": 1, "func": "line_graph", "question":
            "Display a population graph."},
        {"val": 2, "func": "scatter_plot", "question":
            "Display a scatter plot."},
        {"val": 3, "func": "ipython", "question":
            "Leave menu for interactive python session."},
        {"val": 4, "func": "leave", "question": "Quit)."}
        ]

def random_name():
    return "".join(random.choices(string.ascii_letters,
                                  k=random.randrange(1, 10)))

class Test(TestCase):
    def setUp(self):
        self.hello_world = HelloWorld(Resource)
        self.endpoints = Endpoints(Resource)
        self.model = Models(Resource)
        self.props = Props(Resource)
        self.model_menu = ModelMenu(Resource)
        self.run = RunModel(Resource)
        self.models = load_models(indra_dir)

    def test_load_models(self):
        """
        See if models can be loaded.
        """
        rv = self.models
        test_model_file = indra_dir + MODEL_FILE
        with open(test_model_file) as file:
            test_rv = json.loads(file.read())["models_database"]
        self.assertEqual(rv, test_rv)

    def test_hello_world(self):
        """
        See if HelloWorld works.
        """
        rv = self.hello_world.get()
        self.assertEqual(rv, {'hello': 'world'})

    def test_endpoints(self):
        '''
        Check that /endpoints lists these endpoints.
        '''
        endpoints = set(self.endpoints.get()["Available endpoints"])
        test_endpoints = ["/endpoints",
                          "/hello",
                          "/model_creator",
                          "/models",
                          "/models/menu/",
                          "/models/menu/run/<int:run_time>",
                          "/models/props/<int:model_id>"]
        for test_endpoint in test_endpoints:
            # While we could just convert test_endpoints into a set and then
            # check for set equality, this allows the output to show which
            # endpoint was missing.
            with self.subTest(test_endpoint=test_endpoint):
                self.assertIn(test_endpoint, endpoints)

    @skip("The API tests must be re-written: they are locked to a particular format.")
    def test_get_model(self):
        """
        See if we can get models.
        """
        rv = self.model.get()

        test_model_file = indra_dir + MODEL_FILE
        with open(test_model_file) as file:
            test_models_db = json.loads(file.read())["models_database"]

        test_models_response = []
        for model in test_models_db:
            doc = ""
            if "doc" in model:
                doc = model["doc"]
            test_models_response.append({"model ID": model["model ID"],
                                         "name": model["name"],
                                         "doc": doc,
                                         "source": model["source"],
                                         "graph": model["graph"]})

        self.assertEqual(rv, test_models_response)

    @skip("Skipping get props.")
    def test_get_props(self):
        """
        See if we can get props.
        """
        model_id = random.randint(0, 10)
        rv = self.props.get(model_id)

        test_model_file = indra_dir + MODEL_FILE
        with open(test_model_file) as file:
            test_models_db = json.loads(file.read())["models_database"]

        with open(indra_dir + "/" + test_models_db[model_id]["props"]) as file:
            test_props = json.loads(file.read())

        self.assertEqual(rv, test_props)

    @skip("Skipping put props while json format is in flux.")
    def test_put_props(self):
        """
        Test whether we are able to put props
        """
        model_id = random.randint(0, 10)
        with app.test_request_context():
            rv = self.props.put(model_id)
        self.assertEqual(type(rv), dict)

    def test_get_ModelMenu(self):
        """
        Testing whether we are getting the menu.
        """
        rv = self.model_menu.get()
        test_menu_file = indra_dir + "/indra/menu.json"
        with open(test_menu_file) as file:
            test_menu = json.loads(file.read())["menu_database"]
        self.assertEqual(rv, test_menu)

    def test_err_return(self):
        """
        Testing whether we are able to get the right error message
        """
        rv = err_return("error message")
        self.assertEqual(rv, {"Error:": "error message"})


if __name__ == "__main__":
    main()
