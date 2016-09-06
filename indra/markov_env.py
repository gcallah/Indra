"""
markov_env.py

An environment for Markov chain interactions.

"""

# pylint: disable=invalid-name

import indra.grid_env as ge
import indra.markov as markov

X = 0
Y = 1


class MarkovCell(ge.Cell):
    """
    A grid cell that also has a transition matrix
    specific to it.
    """
    def __init__(self, coords, contents=None, trans_matrix=None):
        super().__init__(coords, contents)
        self.trans_matrix = trans_matrix

    def __str__(self):
        return str(self.trans_matrix)


class MarkovEnv(ge.GridEnv):
    """
    An env that holds transition matrix for each cell.
    """

    def __init__(self, name, width, height, trans_str, torus=False,
                 model_nm=None, preact=False, postact=False):
        """
        Create a new markov env
        """
        self.def_trans_matrix = markov.MarkovPre(trans_str)
        super().__init__(name, width, height, torus, preact,
                         postact, model_nm)

    def __new_cell__(self, coords):
        return MarkovCell(coords, trans_matrix=self.def_trans_matrix)

    def get_pre(self, agent):
        cell = self._get_cell(agent.pos[X], agent.pos[Y])
        # print("get pre returning " + str(cell.trans_matrix))
        return cell.trans_matrix

    def set_trans(self, coords, trans):
        cell = self._get_cell(coords[X], coords[Y])
        cell.trans_matrix = trans