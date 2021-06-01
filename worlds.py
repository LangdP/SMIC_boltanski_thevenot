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
                                  {prop: prob for prop, prob in prop_priors.items()
                                   if prop in World(world).properties}]
