# These are the vizualization functions that are used for testing

# Import packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def viz(outcomes, type="speaker", full_results=True):
    cases = {"speaker": speaker_viz,
            "listener": listener_viz}
    return cases.get(type, "Invalid player type")(outcomes)


def speaker_viz(spk_outcomes):
    xlab = "Probability"
    title = "Speaker choice rule probabilities"
    probs = [spk_outcomes[key][0] for key in spk_outcomes]
    probs_alpha = [1 if prob == max(probs) else prob + 0.3 for prob in probs]
    dfs = {key:
           {k: pd.DataFrame({'x': list(spk_outcomes[key][1][k].keys()),
                             'y': list(spk_outcomes[key][1][k].values())})
               for k in spk_outcomes[key][1]}
           for key in spk_outcomes}
    df_pairs = {}
    for df_key in dfs.keys():
        df_pairs[df_key] = []
        for df_k in dfs[df_key]:
            dfs[df_key][df_k]['hue'] = df_k
            df_pairs[df_key].append(dfs[df_key][df_k])
    i = 0
    fig, axs = plt.subplots(len(spk_outcomes), 1, sharex=True)
    fig.suptitle(title)
    for key in df_pairs:
        ylab = key + " (" + str(probs[i])[:3] + ")"
        res = pd.concat(df_pairs[key])
        sns.barplot(x='y', y='x',
                             data=res,
                             hue='hue', 
                             alpha = probs_alpha[i],
                             ax = axs[i])
        axs[i].legend(bbox_to_anchor=(1.02, 1),
                    loc='upper left',
                    borderaxespad=0, )
        axs[i].set(xlabel=xlab, ylabel=ylab) 
        i += 1

    return plt.show()

def listener_viz(lis_outcomes):
    for outcomes in lis_outcomes:
        outcome = lis_outcomes.get(outcomes)
        xlab = "Probability"
        title = "Listener interpretation probabilities"
        probs = [outcome[key][0] for key in outcome]
        probs_alpha = [1 if prob == max(probs) else prob + 0.3 for prob in probs]
        dfs = {key:
            {k: pd.DataFrame({'x': list(outcome[key][1][k].keys()),
                                'y': list(outcome[key][1][k].values())})
                for k in outcome[key][1]}
            for key in outcome}
        df_pairs = {}
        for df_key in dfs.keys():
            df_pairs[df_key] = []
            for df_k in dfs[df_key]:
                dfs[df_key][df_k]['hue'] = df_k
                df_pairs[df_key].append(dfs[df_key][df_k])
        i = 0
        fig, axs = plt.subplots(len(outcome), 1, sharex=True)
        fig.suptitle(title)
        for key in df_pairs:
            ylab = key + " (" + str(probs[i])[:3] + ")"
            res = pd.concat(df_pairs[key])
            sns.barplot(x='y', y='x',
                                data=res,
                                hue='hue', 
                                alpha=probs_alpha[i], 
                                ax = axs[i])
            axs[i].legend(bbox_to_anchor=(1.02, 1),
                        loc='upper left',
                        borderaxespad=0, )
            axs[i].set(xlabel=xlab, ylabel=ylab) 
            i += 1
        plt.show()
