"""
standing_ovation.py
This model simulates how a standing ovation spreads
across an audience. It'll first model whether
a performance gets a standing ovation from at least a
few individual first, and then model how the pressure to
stand or sit affects the rest of the audience.
"""
import random
import indra.display_methods as disp
import indra.markov as markov
import indra.markov_agent as ma
import indra.markov_env as menv

import indra.entity as ent
import indra.env as env

<<<<<<< HEAD
SITTING = "Sitting"
STANDING = "Standing"
NSTATES = 2

=======
>>>>>>> cc2f784705a6e8e1fe755b38bdbad2ca66eb4f9f
class AudienceAgent(ma.MarkovAgent):
    """
    A member of an audience that will decide whether to remain sitting or stand

    Attributes:
        sitting: a boolean indicating whether the member is sitting (T) or standing (F)
        noise: a double that determines the odds of the member following the crowd once
            confronted to make a choice
        standard: a double that determines the odds of the member enjoying the
            performance
    Functions:
        initial: initial reaction to performance. Makes the agent react to the performance
        isSitting: returns a boolean. Checks whether agent is sitting
        setState: takes a boolean state as an argument. Sets agent state to the new state
        reaction: Checks whether the performance was up to the agent's standards
        confront: Forces the agent to react to perceived pressure, will change state if pressure is too much
    """
    def __init__(self, name, goal, noise
<<<<<<< HEAD
                 #, standard = 0.2 #standard could be set by user maybe?
=======
                 #, standard = 0.2 #standard could be set by user
>>>>>>> cc2f784705a6e8e1fe755b38bdbad2ca66eb4f9f
                 ):
        super().__init__(name, goal, NSTATES, SITTING)
        self.name = name
        self.goal = goal
<<<<<<< HEAD
        self.state = SITTING #Everyone starts off sitting
        self.next_state = STANDING
        self.noise = 0.95
        self.standard = 0.2
        self.pressure = 0

        self.initial() #Agent must have a first impression
=======
        self.sitting = True #Everyone starts off sitting
        self.noise = 0.95
        self.standard = 0.2
        self.pressure = 0
        #Agent must have a first impression
        self.initial()
>>>>>>> cc2f784705a6e8e1fe755b38bdbad2ca66eb4f9f

    # Initial reaction to the performance, which will elicit a reaction.
    def initial(self):
        ##maybe performance should be defined elsewhere?
        performance = random.uniform(0.0, 1.0)
        self.reaction(performance)

    def isSitting(self):
        return self.state == SITTING

    def cycleState(self):
        temp = self.state
        self.state = self.next_state
        self.next_state = temp

    # Initial reaction to the performance
        # If the performance falls within the member's standard, the member will stand
    def reaction(self, performance):
        if (performance >= self.standard):
<<<<<<< HEAD
            self.cycleState()

    #Confront the audience member with a decision.
        #If pressure to stand exceeds 50%:
        #Generate a choice value
        #If choice value <= noise
        #the audience member chooses to copy what its neighbors are doing.
    def confront(self):
        choice = random.uniform(0.0, 1.0)
        if(self.pressure > 0.5): #If the pressure is to great, you have a choice
            if (choice <= noise): #If the agent is likely to follow the status quo
                self.cycleState()

    def preact(self):
        different_tot = 0
        neighbors_tot = 0
        for neighbor in self.neighbor_iter():
            if(neighbor.state != self.state):
                different_tot += 1
            neighbors_tot += 1
        self.pressure = different_tot / neighbors_tot

        print("I am agent " + self.name + " and I am looking at my peers [preact]")
=======
            self.setState(False)
            # Member is confronted with the pressure of his neighbors' states. If the choice falls within the noise range

    #Confront the audience member with a decision.
    #If pressure to stand exceeds 50%:
    #Generate a choice value
    #If choice value <= noise
    #the audience member chooses to copy what its neighbors are doing.
    def confront(self):
        if(pressure > 0.5):
            choice = random.uniform(0.0, 1.0)
            if (choice <= noise):
                self.sitting = neighbor_status

    def preact(self):
        standing_tot = 0
        neighbors_tot = 0
        for neighbor in self.neighbor_iter():
            standing_tot += 1
            neighbors_tot += 1
        self.pressure = total_stand / neighbors_tot

        print("I am agent" + self.name + "and I am preacting")
>>>>>>> cc2f784705a6e8e1fe755b38bdbad2ca66eb4f9f

    #With the audience member now having some type of pressure
    #Confront the audience member with the choice of sitting or standing
    def act(self):
        self.confront()
<<<<<<< HEAD
        print("I am agent " + self.name + " and I am reacting to my peers [act]")

    # def postact(self):
    #     print("I am agent" + st
        #self.name + "and sitting = ", self.sitting)
=======
        print("I am agent" + self.name + "and I am reacting to the performance")

    # def postact(self):
    #     print("I am agent" + self.name + "and sitting = ", self.sitting)
>>>>>>> cc2f784705a6e8e1fe755b38bdbad2ca66eb4f9f

# Maybe I'll use something like this later? Maybe a paid audience member
# class Gozer(BasicAgent):
#     """
#     A silly agent that destroys others, for demo purposes
#     """
#
#     def __init__(self):
#         """
#         Init Gozer with slightly different params.
#         """
#         super().__init__(name="Gozer the Destructor", goal="Destroy!")
#
#     def postact(self):
#         """
#         Check to see if we have wiped everyone out.
#         """
#         e = self.env
#         if len(e.agents) == 1:
#             print("Gozer the Destructor has destroyed all!!")
#         else:
#             for agent in e.agents:
#                 if agent is not self:
#                     e.agents.remove(agent)
#                     print("Gozer has destroyed "
#                           + agent.name + "!")
#                     return


class Auditorium(menv.MarkovEnv):
    """
    This environment represents the entire audience
    Arguments:
        width: int
        height: int
    """

    def __init__(self, width, height, model_nm="standing_ovation", props=None):
        #print("I'm in super init")
        super().__init__("Auditorium",
                         width,
                         height,
                         model_nm=model_nm,
                         props=props)

        self.plot_title = "The Audience"

    # def preact_loop(self):
    #     print("Preact loop: demonstrating backwards looping")
    #     for agent in reversed(self.agents): ##What is self.agents? Where does it come from?
    #         print("Agent: " + agent.name + "agent sitting:" + str(agent.sitting))
<<<<<<< HEAD
    def set_agent_color(self):
        # setting our colors adds varieties as well!
        self.set_var_color(SITTING, disp.BLACK)
        self.set_var_color(STANDING, disp.RED)
=======
>>>>>>> cc2f784705a6e8e1fe755b38bdbad2ca66eb4f9f

    def restore_agents(self, json_input):
        for agent in json_input["agents"]:
            self.add_agent(AudienceAgent(agent["name"],
                                      agent["goal"],
                                      agent["noise_level"]))
