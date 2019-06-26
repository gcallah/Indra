"""
Conway's Game of Life model
"""
from random import randint

from propargs.propargs import PropArgs

from indra.agent import Agent, switch
from indra.env import Env
from indra.space import DEF_WIDTH, DEF_HEIGHT
from indra.composite import Composite
from indra.display_methods import BLACK, WHITE, SQUARE

DEBUG = True  # Turns debugging code on or off

groups = None


def create_agent(x, y):
    """
    Create an agent with the passed x, y value as its name.
    """
    name = "(" + str(x) + "," + str(y) + ")"
    return Agent(name=name, action=agent_action)


def change_color(gameoflife_env, agent):
    """
    Automatically change color from one to the other.
    """
    curr_group = agent.primary_group()
    next_group = groups[0]
    if curr_group == next_group:
        next_group = groups[1]
    switch(agent, curr_group, next_group)


def apply_live_rules(gameoflife_env, agent):
    """
    Apply the rules for live agents.
    The agent passed in should be alive.
    """
    print("apply live rules")
    num_live_neighbors = 0
    for neighbor in agent.neighbors:
        if neighbor.primary_group() == groups[1]:
            num_live_neighbors += 1
    if (num_live_neighbors != 2 and num_live_neighbors != 3):
        return True
    else:
        return False


def apply_dead_rules(gameoflife_env, agent):
    """
    Apply the rules for dead agents.
    The agent passed in should be dead.
    """
    num_live_neighbors = 0
    for neighbor in agent.neighbors:
        if neighbor.primary_group() == groups[1]:
            num_live_neighbors += 1
    if num_live_neighbors == 3:
        return True
    else:
        return False


def gameoflife_action(gameoflife_env):
    """
    The action that will be taken every period.
    Loops through every agent, determines whether it is alive or dead,
    and passed it to the corresponding rule function.
    """
    to_be_changed = []
    for y in range(0, gameoflife_env.height):
        for x in range(0, gameoflife_env.width):
            curr_agent = gameoflife_env.get_agent_at(x, y)
            if curr_agent.neighbors is not None:
                if DEBUG:
                    print("Alive neighbors for agent at", curr_agent.get_pos())
                    for i in curr_agent.neighbors:
                        if i.primary_group() == groups[1]:
                            print("     ", i.get_pos())
                if curr_agent.primary_group() == groups[1]:
                    if apply_live_rules(gameoflife_env, curr_agent):
                        to_be_changed.append(curr_agent)
                else:
                    if apply_dead_rules(gameoflife_env, curr_agent):
                        to_be_changed.append(curr_agent)
    for to_change in to_be_changed:
        change_color(gameoflife_env, to_change)


def agent_action(agent):
    if agent.neighbors is None:
        agent.neighbors = gameoflife_env.get_all_neighbors(agent)


def populate_board(gameoflife_env, width, height):
    num_agent = int(0.1 * (width * height))
    upper_limit = int((width / 2) + (width / 4))
    lower_limit = int((width / 2) - (width / 4)) + 1
    for i in range(num_agent):
        agent = gameoflife_env.get_agent_at(randint(lower_limit, upper_limit),
                                            randint(lower_limit, upper_limit))
        if agent.primary_group() != groups[1]:
            change_color(gameoflife_env, agent)


def set_up():
    """
    A func to set up run that can also be used by test code.
    """
    global groups

    pa = PropArgs.create_props('basic_props',
                               ds_file='props/gameoflife.props.json')
    width = pa.get('grid_width', DEF_WIDTH)
    height = pa.get('grid_height', DEF_HEIGHT)
    black = Composite("black", {"color": BLACK, "marker": SQUARE})
    white = Composite("white", {"color": WHITE})
    groups = []
    groups.append(white)
    groups.append(black)
    for y in range(height):
        for x in range(width):
            groups[0] += create_agent(x, y)
    gameoflife_env = Env("game of life env",
                         action=gameoflife_action,
                         height=height,
                         width=width,
                         members=groups,
                         random_placing=False)
    gameoflife_env.user.exclude_choices(["line_graph"])
    populate_board(gameoflife_env, width, height)
    return (groups, gameoflife_env)


def main():
    global groups
    global gameoflife_env
    (groups, gameoflife_env) = set_up()
    gameoflife_env()
    return 0


if __name__ == "__main__":
    main()
