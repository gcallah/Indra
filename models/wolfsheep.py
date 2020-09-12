"""
    This is wolf-sheep re-written in indra.
"""
from random import randint

from indra.agent import Agent
from indra.composite import Composite
from indra.display_methods import TAN, GRAY
from indra.env import Env
from indra.space import SpaceFull
from registry.execution_registry import \
    get_exec_key, init_exec_key
from registry.registry import get_prop, get_group, get_env, get_env_attr
from registry.registry import user_tell, run_notice, user_debug
from indra.utils import init_props

MODEL_NAME = "wolfsheep"
DEBUG = False  # turns debugging code on or off
DEBUG2 = False  # turns deeper debugging code on or off

# some default values:
NUM_WOLVES = 8
NUM_SHEEP = 28
PREY_DIST = 3
MEADOW_HEIGHT = 10
MEADOW_WIDTH = 10

WOLF_LIFESPAN = 5
WOLF_REPRO_PERIOD = 2

SHEEP_LIFESPAN = 8
SHEEP_REPRO_PERIOD = 2

AGT_WOLF_NAME = "wolf"
AGT_SHEEP_NAME = "sheep"

WOLF_GROUP = "wolves"
SHEEP_GROUP = "sheep"

ERR_MSG = "Invalid agent name"

TIME_TO_REPR = "time_to_repr"
TIME_TO_EMIGRATE = "time_to_emigrate"


def isactive(agent, *args):
    """
    See if what wolf is going to eat is alive!
    """
    return agent.is_active()


def eat(agent, prey, **kwargs):
    """
     Wolf's duration increases by sheep's duration
     """
    if DEBUG:
        user_tell(str(agent) + " is eating " + str(prey))
    agent.duration += prey.duration
    rem_agent(prey, **kwargs)


def rem_agent(agent, **kwargs):
    exec_key = get_exec_key(kwargs)
    get_env(execution_key=exec_key).remove_location(agent.get_pos())
    agent.die()


class NoSheep(Exception):
    """
    Exception when all the sheep are eaten up.
    """

    def __init__(self, msg):
        self.message = msg


def get_prey(agent, sheep, **kwargs):
    """
        Wolves eat active sheep from the neighbourhood
    """
    exec_key = get_exec_key(kwargs=kwargs)
    if len(get_group(SHEEP_GROUP, exec_key)) <= 0:
        raise NoSheep("All out of sheep!")

    return get_env(execution_key=exec_key) \
        .get_neighbor_of_groupX(agent,
                                SHEEP_GROUP,
                                hood_size=get_env_attr(
                                    "prey_dist",
                                    execution_key=exec_key))


def reproduce(agent, create_func, group, **kwargs):
    """
    Agents reproduce when TIME_TO_REPR reaches 0
    """
    execution_key = get_exec_key(kwargs=kwargs)
    if agent[TIME_TO_REPR] == 0:
        if DEBUG:
            user_debug(str(agent.name) + " is having a baby!")
        get_env(execution_key=execution_key).add_child(group)
        agent[TIME_TO_REPR] = agent["orig_repr_time"]
        return True
    else:
        return False


def sheep_action(agent, **kwargs):
    execution_key = get_exec_key(kwargs=kwargs)
    agent[TIME_TO_REPR] -= 1
    # sheep can have 1-3 babies at a time
    num_of_babies = randint(1, 3)
    while num_of_babies > 0:
        reproduce(agent, create_sheep,
                  get_group(SHEEP_GROUP, execution_key=execution_key),
                  **kwargs)
        num_of_babies -= 1
    return False


def wolf_action(agent, **kwargs):
    if agent.duration <= 0 or agent.duration == agent[TIME_TO_EMIGRATE]:
        return rem_agent(agent, **kwargs)
    else:
        execution_key = get_exec_key(kwargs=kwargs)
        prey = get_prey(agent,
                        get_group(SHEEP_GROUP, execution_key=execution_key),
                        **kwargs)
        if prey is not None:
            eat(agent, prey, **kwargs)
        agent[TIME_TO_REPR] -= 1
        # wolves can have a litter between 4 & 6 pups
        num_of_babies = randint(4, 6)
        while num_of_babies > 0:
            reproduce(agent, create_wolf,
                      get_group(WOLF_GROUP, execution_key=execution_key),
                      **kwargs)
            num_of_babies -= 1
        agent.duration -= 1
        return False


def create_wolf(name, i, **kwargs):
    """
    Method to create wolf
    """
    execution_key = get_exec_key(kwargs=kwargs)
    time_to_repro = randint(1, WOLF_REPRO_PERIOD)
    time_to_emigrate = randint(1, WOLF_REPRO_PERIOD)
    return Agent(AGT_WOLF_NAME + str(i),
                 duration=WOLF_LIFESPAN,
                 action=wolf_action,
                 attrs={TIME_TO_REPR: time_to_repro,
                        "orig_repr_time": WOLF_REPRO_PERIOD,
                        TIME_TO_EMIGRATE: time_to_emigrate},
                 execution_key=execution_key)


def create_sheep(name, i, **kwargs):
    """
    Method to create sheep
    """
    exec_key = get_exec_key(kwargs=kwargs)
    time_to_repro = randint(1, SHEEP_REPRO_PERIOD)
    return Agent(AGT_SHEEP_NAME + str(i),
                 duration=SHEEP_LIFESPAN,
                 action=sheep_action,
                 attrs={TIME_TO_REPR: time_to_repro,
                        "orig_repr_time": SHEEP_REPRO_PERIOD},
                 execution_key=exec_key)


def set_up(props=None):
    """
    A func to set up run that can also be used by test code.
    """
    init_props(MODEL_NAME, props)
    exec_key = init_exec_key(props)
    members = []
    members.append(Composite(WOLF_GROUP,
                             attrs={"color": TAN},
                             member_creator=create_wolf,
                             num_members=get_prop('num_wolves', NUM_WOLVES,
                                                  execution_key=exec_key),
                             execution_key=exec_key))

    members.append(Composite(SHEEP_GROUP,
                             attrs={"color": GRAY},
                             member_creator=create_sheep,
                             num_members=get_prop('num_sheep', NUM_SHEEP,
                                                  execution_key=exec_key),
                             execution_key=exec_key))

    Env(MODEL_NAME,
        members=members,
        attrs={"prey_dist": get_prop("prey_dist", PREY_DIST,
                                     execution_key=exec_key)},
        height=get_prop('grid_height', MEADOW_HEIGHT,
                        execution_key=exec_key),
        width=get_prop('grid_width', MEADOW_WIDTH,
                       execution_key=exec_key),
        execution_key=exec_key)


def main():
    set_up()
    run_notice(MODEL_NAME)
    try:
        get_env()()
    except (NoSheep, SpaceFull) as excp:
        user_tell(excp)
        user_tell("Halting model.")
    return 0


if __name__ == "__main__":
    main()
