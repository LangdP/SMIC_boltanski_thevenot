# BTmodel

This is the implementation in python of the original model for Boltanski & Thévenot's _De la justification_, to be used in the context of the analysis of sociolinguistic variation and social meaning in the SMIC project. More information on the project can be found [here][smic_url].

[smic_url]: http://www.socialmeaning.eu/


The main inspirations behind those models can be found in Heather Burnett's previous works on Social Meaning Games (SMG) as well as in the book _De la justification: les économies de la grandeur_, by Boltanski and Thévenot. One part of the SMIC project concerns the formal modelling of sociolinguistic variation and the social meaning phenomena associated with it, Boltanski & Thévenot (henceforth B&T) have been chosen as a basis for an attempt at modelling the social world in which actors interact. 

The main idea behind this modelling project is to go beyond the usual treatment that is made of indexed social meaning and add to it a notion of context of enunciation. Instead of simply relying on a preference function over personae (as is the case with standard SMG), the core principle behind the present approach is to condition the indexical meanings of a sociolinguistic variant on the context in which the speaker and listener find themselves at the time of the interaction, and which properties are valued in that context.

# Version 1

Version 1 of the model can be found in the ver_1 folder. It follows the description that was given during the MLLA talk by Heather Burnett given on April 16th 2021, in a slightly simplified manner, only considering _civic, industrial_ and _inspired_ worlds, and only considering the _in'/ing_ variant in English. 

## Explanation

In this model, the context (_world_) in which the interaction occurs (as well as the list of valued personal characteristics in that context) is pre-determined. It is therefore very similar to a simplified version of a SMG, which is itself an expansion on RSA models.

When choosing a sociolinguistic variant, a speaker will take into account the _world_ in which they assume they find themselves and a listener will interpret said variant according to the world they assume they find themselves in as well. If speaker and listener each assume a different world, the interpretations (in terms of properties) available to the listener will not be the same as those intended by the speaker and we can have a _clash_, which would be a case of the intended meaning and the interpreted meaning being mismatched (specifically, to the disadvantage of the listener). 

The code contains 4 classes that mirror some of the objects established in the models : 
1. `World`, a class representing the main objects that describe the contexts. There are 5 different worlds in the MLLA talk (_civic, industrial, inspired, domestic, fame_), only 3 are in this simplified version (first three in the preceding list). Each world, according to its type, is linked to a set of binary qualities ordered from most to least valued. This is hard-coded in the class. In that simplified version, there is only one such binary couple per available world. 

2. `Player`, a general class that then serves as a parent class to `Speaker` and `Listener` classes. It is constructed by specifying a world (in the form of the world's name, a string) and is interpreted to be the ideal literal listener of that world. Its only method is a literal interpretation of the properties.

3. `Speaker`, to be interpreted as the speaker in the formal model; it is a subclass of `Player` and is therefore also constructed with a specified world, as well as a temperature parameter `alpha` (float), which is used during the softmaxing of utilities to determine the choices made by the speaker (basically, the higher the _alpha_, the more _certain_ the speaker is). It has a method to compute the utility of the available messages as well as a `choice_rule(action, messages, prop)` method, which for each variant (`action`) among the list of available variants (`messages`) and given a property (`prop`), says how likely it is that this variant will be chosen over the others to convey that property. 

4. `Listener`, to be interpreted as the listener in the formal model. Again, a subclass of `Player`, it is also constructed using a world name. Because it includes an internal speaker model, it also needs a temperature parameter _alpha_. Its internal speaker is extracted from the same world as the listener is in. Its methods include `lis1(prop, action, messages)`, the arguments of which are defined similarly to what is found in the `Speaker` class `choice_rule` method. 


## Viz

The folder includes a `viz` function, which takes in a list of states and their associated probabilities in the form of a dictionary and displays them in a histogram to vizualize the predictions of the model. The script `testing.py` offers an overview of the various predictions of the model as it was described above. Launching it will generate some plots (but a look at the comments in the script will make things clearer). 

This is obviously a pretty poor/uninteresting example, but it is a start. In the future, and especially when we have more empirical data to discuss these phenomena, we can add more (and more interesting) variables and properties to the model. 

# Version 2

Version 2 of the model changes one key thing in the sense that the contexts (or _worlds_) are no longer deterministically defined prior to doing the computations, but instead each speaker/listener has an internal probability distribution over worlds. 

## Explanation

The bulk of the model is similar to version 1, but the addition of priors over worlds changes a few things in the definitions of certain classes (notably the `World` class) and methods. Instances of the `Speaker` and `Listener` classes are now also constructed with a set of priors from the new `Priors` class, which is constructed using two dictionaries containing priors over worlds and over properties and formats them correctly for use with the methods of speakers and listeners. It is basically a specific kind of dictionary. 

The `Speaker` and `Listener` classes have most of their methods modified to take into account the addition of world priors and also have supplementary methods. Specifically, both have acquired a `predictions` and `full_predictions` method. The first of these gives a specific prediction when the world is fixed (basically, an implementation of what we had in the `testing.py` script in version 1 for the formatting of the results). The second one does the same thing, but it iterates it over worlds and gives the full results for each world along with the prior probability of that world. 

Both of these methods output an object of the format required by the new `viz` function.

The `Listener` class also has a new method, `update_world_priors(utt, messages)` which updates the priors beliefs over worlds of the listener when a specific utterance (`utt`, string) from the set of utterances we're considering (`messages`, list) is heard. The function for prior update is a bit shady right now, but it does work as intended and gives appropriate results, it is just not easy to justify, philosophically. How strong this update is is determined by another temperature parameter, _beta_ (float), which is necessary to construct an instance of the Listener class.

Keep in mind when playing with it that this method is called when asking for a listener's `full_predictions`, so in case you will generate the plots several times, the results will take those updates into account (a good practice then would be to use `viz` on a variable containing the predictions and not re-run the method everytime, as in `viz(listener.full_predictions(...))`).
## Viz

I recommend to use `viz` on the objects generated by `full_predictions` to see the actual changes from the first version of the model. When doing so, one will see a plot representing the probability of using one variant over the other, given a preferred property (speakers) or the probability of interpreting one property over another having heard a specific variant (listener), over all 5 worlds, with the appropriate properties for each world. 
The world that is deemed to be the most probable for the interaction is highlighted. For listeners, the `viz` function actually generates two plots, because the priors are not the same according to which variant was just heard (so the highlighting will differ.)
