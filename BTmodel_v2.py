# This program is the first implementation of the BT models
# that we use in the SMIC project, see README for more info

from math import exp, log

# This is to avoid value errors when computing utilities


def my_log(n):
    if n == 0:
        return -9999999
    else:
        return log(n)

# This is the world class. It is supposed to represent worlds in the model
# , along with their attributes (mostly orders of worth).
# The orders of worth have to be set manually right now, but once we have
# all the properties we're interested in along with the orders of worth, we can
# easily generate a world only using its name.


class World:
    def __init__(self, world_name) -> None:
        self.world_name = world_name

        # Here we set the properties we're interested in for each world
        # In the second version of the model, this could be the FUN thing
        # Maybe I will make it more complex in the future, including
        # probabilities on this too, but right now let's keep it like this.

        if self.world_name == "industrial":
            self.properties = ["competent", "incompetent"]
        elif self.world_name == "civic":
            self.properties = ["friendly", "unfriendly"]
        elif self.world_name == "inspired":
            self.properties = ["insightful", "uninsightful"]

        # We set the order of worth as a list. Right now this is not very
        # interesting because it's not clear to me how we're gonna use the
        # orders of worth anyway, but I still put it in the only way I
        # could make sense of it
        self.order_of_worth = [self.properties[0], self.properties[1]]

        # This links variants to properties, depending on the world we're in
        if self.world_name == "industrial":
            self.interpretation_function = {"ing": [self.properties[0]],
                                            "in": [self.properties[1]]}
        elif self.world_name == "civic":
            self.interpretation_function = {"ing": [self.properties[1]],
                                            "in": [self.properties[0]]}
        elif self.world_name == "inspired":
            self.interpretation_function = {"ing": [self.properties[0], self.properties[1]],
                                            "in": [self.properties[0], self.properties[1]]}

# This class is the priors, it is a special kind of dictionary to make it
# easy to store the priors for each player in the correct format.
class Priors:
    def __init__(self, world_priors, prop_priors) -> None:
        self.world_priors = world_priors
        self.prop_priors = prop_priors
        self.priors = {}
        for world in world_priors:
            self.priors[world] = [world_priors[world], 
                                {prop:prob for prop, prob in prop_priors.items() 
                                if prop in World(world).properties}]



# This is our Player class. I assume that from a cognitive standpoint it makes
# sense that all players have access to literal meanings, so I put them there
# Otherwise not very interesting
class Player:
    def __init__(self, priors) -> None:
        # These are the full priors for the player, the .priors attr
        # of a Priors object
        self.priors = priors.priors


    def conditionalization(self, world, prop, utt):
        wworld = World(world)
        interpret = lambda utt, prop :  1 \
            if prop in wworld.interpretation_function[utt]\
             else 0
        prop_given_mw = ((interpret(utt, prop))
                        / (sum([interpret(utt, prop) for prop in wworld.properties])))
        return prop_given_mw


# This is the Speaker class, it takes a world and a temperature parameter as
# arguments. It inherits the literal interpretations from the player class.
class Speaker(Player):
    def __init__(self, priors, alpha) -> None:
        super().__init__(priors)
        self.alpha = alpha

    def utility(self, world, prop, utt):
        return my_log(self.conditionalization(world, prop, utt) * self.priors[world][0])

    def choice_rule(self, world, utt, messages, prop):
        return (exp(self.alpha * self.utility(world, prop, utt))
                / sum([exp(self.alpha * self.utility(world, prop, message)) for message in messages]))


# This is the Listener class. Not much to say here except that this layout makes
# it clear that the listener envisions the speaker as belonging to the same
# world as them, which is not necessarily true and something we might want
# to play with once we have more of an idea how clashes work.
# In any case, each listener envisions their own player.
class Listener(Player):
    def __init__(self, priors, alpha, beta) -> None:
        super().__init__(priors)
        self._speaker = Speaker(priors, alpha)
        self.alpha = alpha
        self.beta = beta

    def lis(self, world, prop, utt, messages):
        return ((self.priors[world][1][prop] * self._speaker.choice_rule(world, utt, messages, prop)) /
                sum([self.priors[world][1][p] * self._speaker.choice_rule(world, utt, messages, p)
                     for p in World(world).properties]))
    
    def update_world_priors(self, utt, messages):
        scores = []
        for w in self.priors:
            for p in World(w).properties:
                if World(w).order_of_worth.index(p) == 0:
                    score = self.priors[w][0] + self.priors[w][0] * self.lis(w, p, utt, messages) 
                else:
                    pass
            scores.append(score)
        i = 0
        for w in self.priors:
            self.priors[w][0] = (exp(self.beta * scores[i]) / 
                sum([exp(self.beta * score) for score in scores]))
            i += 1

