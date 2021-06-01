# These are the vizualization functions that are used for testing

# Import packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def viz(outcomes, type="speaker", full_results=True):
    cases = {"speaker": speaker_viz(outcomes),
            "listener": "Not yet"}
    return cases.get(type, "Invalid player type")


def speaker_viz(outcomes):
    xlab = "Probability"
    title = "Speaker choice rule probabilities"
    probs = [outcomes[key][0] for key in outcomes]
    probs_alpha = []
    dfs = {key:
           {k: pd.DataFrame({'x': list(outcomes[key][1][k].keys()),
                             'y': list(outcomes[key][1][k].values())})
               for k in outcomes[key][1]}
           for key in outcomes}
    df_pairs = {}
    for df_key in dfs.keys():
        df_pairs[df_key] = []
        for df_k in dfs[df_key]:
            dfs[df_key][df_k]['hue'] = df_k
            df_pairs[df_key].append(dfs[df_key][df_k])
    i = 0
    fig, axs = plt.subplots(len(outcomes), 1, sharex=True)
    fig.suptitle(title)
    for key in df_pairs:
        ylab = key + " (" + str(probs[i])[:3] + ")"
        res = pd.concat(df_pairs[key])
        sns.barplot(x='y', y='x',
                             data=res,
                             hue='hue', 
                             ax = axs[i])
        axs[i].legend(bbox_to_anchor=(1.02, 1),
                    loc='upper left',
                    borderaxespad=0, )
        axs[i].set(xlabel=xlab, ylabel=ylab) 
        i += 1

    return plt.show()
