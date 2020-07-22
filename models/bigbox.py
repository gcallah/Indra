"""
Big box model for simulating the behaviors of consumers.
"""

import random

from indra.agent import Agent
from indra.composite import Composite
from indra.display_methods import BLACK, BLUE, GRAY, GREEN, RED, TAN, YELLOW
from indra.env import Env
from registry.registry import get_env, get_prop, get_group, set_env_attr
from indra.space import DEF_HEIGHT, DEF_WIDTH
from indra.utils import init_props

MODEL_NAME = "bigbox"
NUM_OF_CONSUMERS = 50
NUM_OF_MP = 8
DEBUG = False

CONSUMER_INDX = 0
BB_INDX = 1

HOOD_SIZE = 2
MP_PREF = 0.1
PERIOD = 7
STANDARD = 200
MULTIPLIER = 10

EXPENSE_INDX = 0
CAPITAL_INDX = 1
COLOR_INDX = 2

mp_pref = None
hood_size = None
bb_capital = 2000

period = None
store_census = None

# The data below creates store types with default values.
# "Store type":
# [expense, capital, color]
mp_stores = {"Bookshop": [65, 90, TAN],
             "Coffeeshop": [63, 100, BLACK],
             "Grocery store": [67, 100, GREEN],
             "Hardware": [60, 110, RED],
             "Restaurant": [60, 100, YELLOW]}


def sells_good(store, consumer):
    """
    Check if the store sells what the consumer wants.
    If BB return True else return whether seller sells that type.
    """
    if store.primary_group() == get_group(BB_INDX):
        return True
    else:
        if consumer["item needed"] in store.name:
            return True
        return False


def get_rand_good_type():
    """
    Randomly select consumer's item needed
    after each run.
    """
    return random.choice(list(mp_stores.keys()))


def create_consumer(name, i, props=None):
    """
    Create consumers
    """
    spending_power = random.randint(50, 70)
    consumer_books = {"spending power": spending_power,
                      "last util": 0.0,
                      "item needed": get_rand_good_type()}
    return Agent(name + str(i), attrs=consumer_books, action=consumer_action)


def create_mp(store_type, i):
    """
    Create a mom and pop store.
    """
    expense = mp_stores[str(store_type)]
    name = str(store_type) + " " + str(i)
    store_books = {"expense": expense[EXPENSE_INDX],
                   "capital": expense[CAPITAL_INDX]}
    return Agent(name=name, attrs=store_books, action=mp_action)


def create_bb(name):
    """
    Create a big box store.
    """
    global bb_capital

    bb_book = {"expense": 150,
               "capital": bb_capital}
    return Agent(name=name, attrs=bb_book, action=bb_action)


def bb_action(bb):
    """
    Deduct expenses from the capital of big box and
    check if big box goes out of business.
    """
    return common_action(bb)


def get_util(store):
    """
    Get utility depending on the store type.
    """
    global mp_pref

    if store.primary_group() == get_group(BB_INDX):
        return calc_util(store)
    else:
        return calc_util(store) + mp_pref


def consumer_action(consumer):
    """
    Check shops near consumer and
    consumer decide where to shop at.
    """
    global hood_size
    nearby_neighbors = get_env().get_moore_hood(
        consumer, hood_size=hood_size)
    store_to_go = None
    max_util = 0.0
    for neighbors in nearby_neighbors:
        neighbor = nearby_neighbors[neighbors]
        if (neighbor.is_active() and (neighbor.primary_group()
                                      != get_group(CONSUMER_INDX))):
            if sells_good(neighbor, consumer):
                curr_store_util = get_util(neighbor)
                if curr_store_util > max_util:
                    max_util = curr_store_util
                    store_to_go = neighbor
    if store_to_go is not None:
        transaction(store_to_go, consumer)
        if DEBUG:
            print("     someone shopped at ", store_to_go)
    consumer["item needed"] = get_rand_good_type()
    return False


def transaction(store, consumer):
    """
    Add money to the store's capital from consumer.
    """
    store["capital"] += consumer["spending power"]
    # print("   ", consumer, "spend money at ", store)


def calc_util(stores):
    """
    calculate utility for stores.
    """
    return random.random()


def mp_action(mp):
    """
    Deduct expenses from mom and pop stores and
    check if mom and pop store goes out of business.
    """

    return common_action(mp)


def common_action(obj):
    """
    Common action to deduct expenses and
    check whether the entity goes out of business
    """
    obj["capital"] -= obj["expense"]
    if DEBUG:
        print("       ", obj, "has a capital of ", obj["capital"])
    if obj["capital"] <= 0:
        obj.die()
        if DEBUG:
            print("       ", obj, "is out of business.")
    return True


def town_action(town):
    """
    check the period and decide when to add
    the big box store
    """
    global period
    box = get_env()
    if town.get_periods() == period:
        new_bb = create_bb("Big Box")
        #set_env_attr()
        #groups[BB_INDX] += new_bb
        # How do we add group to the environment
        box.attrs["bb_group"] += 1
        town.place_member(new_bb)


def set_up(props=None):
    """
    Create an Env for Big box.
    """
    global mp_pref
    global hood_size
    global store_census
    global period
    global bb_capital
    # set_env_attr , gget_attr 

    init_props(MODEL_NAME, props)

    width = get_prop("grid_width", DEF_WIDTH)
    height = get_prop("grid_height", DEF_HEIGHT)
    num_consumers = get_prop("consumer_num", NUM_OF_CONSUMERS)
    num_mp = get_prop("mp_num", NUM_OF_MP)
    mp_pref = get_prop("mp_pref", MP_PREF)
    hood_size = get_prop("hood_size", HOOD_SIZE)
    multiplier = get_prop("multiple", MULTIPLIER)
    bb_capital = multiplier * STANDARD
    period = get_prop("period", PERIOD)

    consumer_group = Composite("Consumer", {"color": GRAY},
                               member_creator=create_consumer,
                               num_members=num_consumers)
    bb_group = Composite("Big box", {"color": BLUE})
    #groups = [consumer_group, bb_group]
    groups = []
    for stores in range(0, len(mp_stores)):
        store_name = list(mp_stores.keys())[stores]
        groups.append(Composite(store_name,
                                {"color": mp_stores[store_name][COLOR_INDX]}))
    for m in range(0, num_mp):
        rand = random.randint(2, len(groups) - 1)
        groups[rand] += create_mp(groups[rand], m)
    Env("Town",
        action=town_action,
        members=groups,
        height=height,
        width=width)
    set_env_attr("consumer_group", consumer_group)
    set_env_attr("bb_group", bb_group)
    return (groups)


def main():

    set_up()
    get_env()()
    return 0


if __name__ == "__main__":
    main()
