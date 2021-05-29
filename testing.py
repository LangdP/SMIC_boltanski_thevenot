# Import packages

from BTmodel_v2 import *

world_priors = {
    "civic": 1/3,
    "industrial": 1/3,
    "inspired": 1/3#,
 #   "domestic": 1/5,
 #   "fame": 1/5,
    }

prop_priors = {
    "competent":0.5,
    "incompetent":0.5,
    "friendly":0.5,
    "unfriendly":0.5,
    "insightful":0.5,
    "uninsightful":0.5
}

priors = Priors(world_priors, prop_priors)

speaker = Speaker(priors, 1)
messages = ["in", "ing"]

speaker.choice_rule("civic", "ing", messages, "friendly")

listener = Listener(priors, 1, .5)

listener.lis("inspired", "insightful", "in", messages)

print(listener.priors)

i = 0
while i < 5:
    listener.update_world_priors("in", messages)
    print(listener.priors)
    i+=1