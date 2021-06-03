# Import packages
from BTmodel_v1 import *
from viz_functions import *


# Setting those for an example. This is obviously a fairly uninteresting example
# but we can still see that things work fine.


# These are our messages. Right now this is the only variation that is taken into
# account in the implementation. 
messages = ["ing", "in"]


# We first instantiate a speaker and a listener from the same world.
industrial_speaker = Speaker("industrial", 1)
industrial_listener = Listener("industrial", 1)

# The props variable could just be referred to as World(world_name).properties,
# but I made it more explicit for clarity here.
# In fact, the methods calling for props could be switched to calling for the 
# properties of the appropriate world directly in the method, but for a first
# implementation, it felt a bit black-boxy. 

props = ["competent", "incompetent"]
indus_speaker_pred = {m: industrial_speaker.choice_rule(m, messages, props[0])
                      for m in messages}

# We can use the viz function for detailed look at one case
viz(indus_speaker_pred, full_results=False)

# Now we build dictionaries of the right format for a fuller vizualization
indus_speaker_pred = {p:
                      {m: industrial_speaker.choice_rule(m, messages, p)
                       for m in messages}
                      for p in props}

indus_listener_pred = {m:
                      {p: industrial_listener.lis1(p, m, messages)
                       for p in props}
                      for m in messages}
# We can also use the viz function to generate a barplot with many cases
viz(indus_speaker_pred)
viz(indus_listener_pred, type="listener")


# And now we do it with other worlds.
# Civic world 

civic_speaker = Speaker("civic", 1)
civic_listener = Listener("civic", 1)

props = ["friendly", "unfriendly"]
civic_speaker_pred = {p:
                      {m: civic_speaker.choice_rule(m, messages, p)
                       for m in messages}
                      for p in props}
civic_listener_pred = {m:
                      {p: civic_listener.lis1(p, m, messages)
                       for p in props}
                      for m in messages}
viz(civic_speaker_pred)
viz(civic_listener_pred, type="listener")


# Inspired world

inspired_speaker = Speaker("inspired", 1)
inspired_listener = Listener("inspired", 1)

props = ["insightful", "uninsightful"]
inspired_speaker_pred = {p:
                         {m: inspired_speaker.choice_rule(m, messages, p)
                          for m in messages}
                         for p in props}
inspired_listener_pred = {m:
                      {p: inspired_listener.lis1(p, m, messages)
                       for p in props}
                      for m in messages}
viz(inspired_speaker_pred)
viz(inspired_listener_pred, type="listener")
