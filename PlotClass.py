import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import inspect


class Plot:

    def __init__(self):
        self.data = pd.read_json('deviation.json')

    def draw_plots(self):
        self.draw_plot_normal_distribution()
        self.draw_plot_dependency_mean()
        self.draw_plot_act_and_pred_corners()
        self.draw_plot_density_points()

    def draw_plot_normal_distribution(self):
        ax = sns.kdeplot(data=self.data[['rb_corners', 'gt_corners']], fill=True,
                         common_norm=False, palette="rocket", alpha=.3, linewidth=0, multiple="stack")
        ax.set(title='Normal distribution in actual and prediction values')

        path = f'plots/{inspect.stack()[0][3]}.png'
        ax.figure.savefig(path)
        return path

    def draw_plot_dependency_mean(self):
        fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=True)
        fig.suptitle('Dependence of global mean from floor_mean and ceiling_mean')

        sns.scatterplot(ax=axes[0], data=self.data, x='floor_mean', y='mean', hue='rb_corners', palette="pastel")
        axes[0].set_title('Dependence of global mean from floor_mean')

        sns.scatterplot(ax=axes[1], data=self.data, x='ceiling_mean', y='mean', hue='rb_corners', palette="pastel")
        axes[1].set_title('Dependence of global mean from ceiling_mean')

        path = f'plots/{inspect.stack()[0][3]}.png'
        fig.figure.savefig(path)
        return path

    def draw_plot_act_and_pred_corners(self):
        ax = sns.lmplot(x='rb_corners', y='gt_corners', data=self.data, line_kws={"color": "C3"})
        ax.set(title='Actual and Prediction number of corners')
        path = f'plots/{inspect.stack()[0][3]}.png'
        ax.figure.savefig(path)
        return path

    def draw_plot_density_points(self):
        ax = sns.swarmplot(data=self.data, x='rb_corners', y='mean', size=3.5, hue="rb_corners", palette='pastel')
        ax.set(ylabel="Density", title="Density points around main corners")
        path = f'plots/{inspect.stack()[0][3]}.png'
        ax.figure.savefig(path)
        return path
