
# Import packages

from players import *
from worlds import *
from helpers import *
from viz import *

# Define priors over worlds here

world_priors = {
    "civic": 1/3,
    "industrial": 1/3,
    "inspired": 1/3#,
 #   "domestic": 1/5,
 #   "fame": 1/5,
    }

# Define priors over properties here
prop_priors = {
    "competent":0.5,
    "incompetent":0.5,
    "friendly":0.5,
    "unfriendly":0.5,
    "insightful":0.5,
    "uninsightful":0.5
}

# Build priors
priors = Priors(world_priors, prop_priors)

speaker = Speaker(priors, 1)
messages = ["in", "ing"]
listener = Listener(priors, 1, 1)

viz(speaker.full_predictions(messages))