#Import packages
from BTmodel import *
from viz_functions import *


# Setting those for an example. The data can now be explored from the command line.
# I will work on more legible graphical renderings of it soon, but everything seems
# to be working fine. Obviously this is not a very interesting example, so we'd have
# to find a better one.

# These are our messages
messages = ["ing", "in"]


industrial_speaker = Speaker("industrial", 1)
industrial_listener = Listener("industrial", 1)

props = ["competent", "incompetent"]
indus_speaker_pred = {m : industrial_speaker.choice_rule(m, messages, props[0]) 
    for m in messages}

# We can use the viz function for detailed look at one case
viz(indus_speaker_pred)

indus_speaker_pred = {p : 
    {m : industrial_speaker.choice_rule(m, messages, p) 
        for m in messages} 
    for p in props}

# We can also use it to generate barplot with many cases
viz(indus_speaker_pred)

civic_speaker = Speaker("civic", 1)
civic_listener = Listener("civic", 1)

props = ["friendly", "unfriendly"]
civic_speaker_pred = {p : 
    {m : civic_speaker.choice_rule(m, messages, p) 
        for m in messages} 
    for p in props}
viz(civic_speaker_pred)

inspired_speaker = Speaker("inspired", 1)
inspired_listener = Listener("inspired", 1)

props = ["insightful", "uninsightful"]
inspired_speaker_pred = {p : 
    {m : inspired_speaker.choice_rule(m, messages, p) 
        for m in messages} 
    for p in props}
viz(inspired_speaker_pred)