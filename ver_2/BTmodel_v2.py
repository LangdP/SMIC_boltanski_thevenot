# Import packages

from players import *
from worlds import *
from helpers import *
from viz import *

# Define priors over worlds here, they have to add up to 1.
uniform_world_priors = {
    "civic": 1 / 5,
    "industrial": 1 / 5,
    "inspired": 1 / 5,
    "domestic": 1 / 5,
    "fame": 1 / 5,
}

industrial_world_priors = {
    "civic": 0.05,
    "industrial": 0.8,
    "inspired": 0.05,
    "domestic": 0.05,
    "fame": 0.05,
}
# Define priors over properties here. For each pair of properties the priors have
# to add up to 1.
prop_priors = {
    "competent": 0.5,
    "incompetent": 0.5,
    "friendly": 0.5,
    "unfriendly": 0.5,
    "insightful": 0.5,
    "uninsightful": 0.5,
    "cool": 0.5,
    "uncool": 0.5,
    "traditional": 0.5,
    "non-traditional": 0.5,
}

# Build priors as an instance of the Priors class.
uniform_priors = Priors(uniform_world_priors, prop_priors)
industrial_priors = Priors(industrial_world_priors, prop_priors)

# This is our list of variants/messages.
messages = ["ing", "in"]

# We construct our Speaker and Listener objects. They share the same priors here
# but we can make custom priors for each.
speaker = Speaker(uniform_priors, 1)
speaker_predictions = speaker.full_predictions(messages)
listener = Listener(industrial_priors, 1, 3)
listener_predictions = listener.full_predictions(messages)


# Here are the vizualizations.
viz(speaker_predictions)
viz(listener_predictions, type="listener")
