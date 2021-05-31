# This script contains the vizualization functions for the model.


# Import packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def viz(outcomes, type="speaker", full_results=True):
    # This function takes in a series of states and their probabilities
    # in the form of a dictionary and gives out a histogram representing them.
    ylab = "Probability"
    if type == "listener":
        xlab = "Properties"
        title = "Listener interpretations"
    else:
        xlab = "Utterances"
        title = "Speaker intentions"

    if full_results:
        dfs = {key: pd.DataFrame({'x': list(outcomes[key].keys()),
                                 'y': list(outcomes[key].values())}) for key in outcomes}
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
