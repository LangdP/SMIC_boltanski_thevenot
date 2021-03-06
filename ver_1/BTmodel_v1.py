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


# This is our Player class. I assume that from a cognitive standpoint it makes
# sense that all players have access to literal meanings, so I put them there
# Otherwise not very interesting
class Player:
    def __init__(self, world) -> None:
        self.world = World(world)
        # These are the priors over properties. Right now, they have to be set manually
        # surely we want this to be easily parameterized in the future, that way it would
        # allow us to have different priors for speaker and listener, which is not possible
        # right now
        self.prior_prop = {
            self.world.properties[0]: 0.5, self.world.properties[1]: 0.5}

    def conditionalization(self, prop, action):
        def interpret(
            utt, prop): return 1 if prop in self.world.interpretation_function[utt] else 0
        prop_given_m = ((interpret(action, prop))
                        / (sum([interpret(action, prop) for prop in self.world.properties])))
        return prop_given_m


# This is the Speaker class, it takes a world and a temperature parameter as
# arguments. It inherits the literal interpretations from the player class.
class Speaker(Player):
    def __init__(self, world, alpha) -> None:
        super().__init__(world)
        self.alpha = alpha

    def utility(self, prop, action):
        return my_log(self.conditionalization(prop, action))

    def choice_rule(self, action, messages, prop):
        return (exp(self.alpha * self.utility(prop, action))
                / sum([exp(self.alpha * self.utility(prop, message)) for message in messages]))


# This is the Listener class. Not much to say here except that this layout makes
# it clear that the listener envisions the speaker as belonging to the same
# world as them, which is not necessarily true and something we might want
# to play with once we have more of an idea how clashes work.
# In any case, each listener envisions their own player.
class Listener(Player):
    def __init__(self, world, alpha) -> None:
        super().__init__(world)
        self._speaker = Speaker(world, alpha)

    def lis0(self, prop, action):
        return self.conditionalization(prop, action)

    def lis1(self, prop, action, messages):
        return ((self.prior_prop[prop] * self._speaker.choice_rule(action, messages, prop)) /
                sum([self.prior_prop[p] * self._speaker.choice_rule(action, messages, p)
                     for p in self.world.properties]))
