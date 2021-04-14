#This program is the first implementation of the BT models
#that we use in the SMIC project, see README for more info

from math import exp, log

class World:
    def __init__(self, world_name) -> None:
        self.world_name = world_name

        if self.world_name == "industrial":
            self.properties = ["competent", "incompetent"]
        elif self.world_name == "civique":
            self.properties = ["friendly", "unfriendly"]
        elif self.world_name == "inspired":
            self.properties = ["insightful", "uninsightful"]
        
        self.order_of_worth = [self.propeties[0], self.properties[1]]
        
        if self.world_name == "industrial":
            self.interpretation_function = {"ing":[self.properties[0]], 
                                            "in":[self.properties[1]]}
        elif self.world_name == "civique":
            self.interpretation_function = {"ing":[self.properties[1]], 
                                            "in":[self.properties[0]]}
        elif self.world_name == "inspired":
            self.interpretation_function = {"ing":[self.properties[0], self.properties[1]], 
                                            "in":[self.properties[0], self.properties[1]]}


class Player:
    def __init__(self, messages, world) -> None:
        self.messages = messages
        self.world = World(world)

        self.prior_prop = {self.world.properties[0]:0.5, self.world.properties[1]:0.5}
    def conditionalization(self, prop, action):
        interpret = lambda utt, prop: 1 if prop in self.world.interpretation_function[utt] else 0
        prop_given_m = (interpret(action, prop)/sum(interpret))





        self.prior_properties = {self.properties[0]:0.5, self.properties[1]:0.5}


def main():


if __name__ == "__main__":
    main()