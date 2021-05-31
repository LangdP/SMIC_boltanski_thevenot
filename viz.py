# These are the vizualization functions that are used for testing

# Import packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def viz(outcomes, type="speaker", full_results=True):
    ylab = "Probability"
    if type == "listener":
        xlab = "Properties"
        title = "Listener interpretations"
    else:
        xlab = "Utterances"
        title = "Speaker intentions"

    if full_results:
        dfs = {key: pd.DataFrame({'x': list(outcomes[key][1].keys()),
                                 'y': list(outcomes[key][1].values())}) for key in outcomes}
        df_list = []
        for df_key in dfs.keys():
            dfs[df_key]['hue'] = df_key
            df_list.append(dfs[df_key])

        res = pd.concat(df_list)
        ax = sns.barplot(x='x', y='y',
                         data=res,
                         hue='hue')
        ax.set(xlabel=xlab, ylabel=ylab, title=title)
        ax.legend(bbox_to_anchor=(1.01, 1),
                  borderaxespad=0, )
        plt.tight_layout()
        return plt.show()
    else:
        plt.bar(outcomes.keys(), outcomes.values())
        return plt.show()


def speaker_viz(outcomes):
    probs = [outcomes[key][0] for key in outcomes]
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
    for key in df_pairs:
        res = pd.concat(df_pairs[key])
        fig, axs = plt.subplots(len(outcomes), 1, sharex=True, squeeze=False)
        sns.barplot(x='x', y='y',
                             data=res,
                             hue='hue', 
                             ax = axs[i][0])
        i += 1

    return plt.show()
