
# Import packages

from players import *
from worlds import *
from helpers import *
from viz import *

# Define priors over worlds here

world_priors = {
    "civic": 1/5,
    "industrial": 1/5,
    "inspired": 1/5,
    "domestic": 1/5,
    "fame": 1/5,
    }

# Define priors over properties here
prop_priors = {
    "competent":0.5,
    "incompetent":0.5,
    "friendly":0.5,
    "unfriendly":0.5,
    "insightful":0.5,
    "uninsightful":0.5,
    "cool":0.5,
    "uncool":0.5,
    "traditional":0.5,
    "non-traditional":0.5
}

# Build priors
priors = Priors(world_priors, prop_priors)

messages = ["in", "ing"]
speaker = Speaker(priors, 1)
speaker_predictions = speaker.full_predictions(messages)
listener = Listener(priors, 1, 1)
listener_predictions = listener.full_predictions(messages)


viz(speaker_predictions)
viz(listener_predictions, type="listener")