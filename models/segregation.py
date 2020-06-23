"""
Schelling's segregation model.
"""

import random

from indra.agent import Agent
from indra.composite import Composite
from indra.display_methods import RED, BLUE
from indra.env import Env
from registry.registry import get_env, get_prop
from registry.registry import run_notice
from indra.utils import init_props

MODEL_NAME = "segregation"
DEBUG = True  # Turns debugging code on or off
DEBUG2 = False  # Turns deeper debugging code on or off

NUM_RED = 250
NUM_BLUE = 250

DEF_CITY_DIM = 40

TOLERANCE = "tolerance"
DEVIATION = "deviation"
COLOR = "color"

DEF_HOOD_SIZE = 1
DEF_TOLERANCE = .5
DEF_SIGMA = .2

MAX_TOL = 0.1
MIN_TOL = 0.9

BLUE_TEAM = 0
RED_TEAM = 1

HOOD_SIZE = 4

NOT_ZERO = .001

BLUE_AGENTS = "Blue agents"
RED_AGENTS = "Red agents"

group_names = [BLUE_AGENTS, RED_AGENTS]

hood_size = None

opp_group = None


def get_tolerance(default_tolerance, sigma):
    tol = random.gauss(default_tolerance, sigma)
    # a low tolerance number here means high tolerance!
    tol = max(tol, MAX_TOL)
    tol = min(tol, MIN_TOL)
    return tol


def my_group_index(agent):
    return int(agent[COLOR])


def other_group_index(agent):
    return not my_group_index(agent)


def env_favorable(hood_ratio, my_tolerance):
    """
    Is the environment to our agent's liking or not??
    """
    return hood_ratio >= my_tolerance


def seg_agent_action(agent):
    """
    If the agent is surrounded by more "others" than it
    is comfortable with, the agent will move.
    """
    agent_group = agent.primary_group()
    ratio_same = 0
    neighbors = get_env().get_moore_hood(agent, hood_size=agent['hood_size'])
    num_same = 0
    for neighbor in neighbors:
        if neighbors[neighbor].primary_group() == agent_group:
            num_same += 1
    if len(neighbors) != 0:
        ratio_same = num_same / len(neighbors)
    return env_favorable(ratio_same, agent[TOLERANCE])


def create_resident(name, i):
    """
    Creates agent of specified color type
    """

    if "Blue" in name:
        color = 0
        mean_tol = get_prop('mean_tol', DEF_TOLERANCE)
    else:
        color = 1
        mean_tol = -get_prop('mean_tol', DEF_TOLERANCE)
    dev = get_prop('deviation', DEF_SIGMA)
    this_tolerance = get_tolerance(mean_tol,
                                   dev)
    return Agent(name + str(i),
                 action=seg_agent_action,
                 attrs={TOLERANCE: this_tolerance,
                        COLOR: color, "hood_changed": True,
                        "just_moved": False,
                        "hood_size": get_prop('hood_size',
                                              DEF_HOOD_SIZE)
                        }, )


def set_up(props=None):
    """
    A func to set up run that can also be used by test code.
    """
    init_props(MODEL_NAME, props)
    blue_agents = Composite(group_names[BLUE_TEAM],
                            {"color": BLUE},
                            member_creator=create_resident,
                            num_members=get_prop('num_blue',
                                                 NUM_BLUE))
    red_agents = Composite(group_names[RED_TEAM],
                           {"color": RED},
                           member_creator=create_resident,
                           num_members=get_prop('num_red', NUM_RED))
    city = Env(MODEL_NAME, members=[blue_agents, red_agents],
               height=get_prop('grid_height', DEF_CITY_DIM),
               width=get_prop('grid_width', DEF_CITY_DIM))
    city.exclude_menu_item("line_graph")


def main():
    set_up()
    run_notice(MODEL_NAME)
    # get_env() returns a callable object:
    get_env()()
    return 0


if __name__ == "__main__":
    main()
