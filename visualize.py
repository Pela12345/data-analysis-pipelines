import matplotlib
import matplotlib.pyplot as plt
import analysis
import seaborn as sns

def growth_plot(data_merged, variable, heading):
    data5 = data_merged.groupby([variable]).agg({"Casualties": "sum", "Attacks": "sum"})
    gplot = data5
    if variable == "Year":
        gplot.plot.line(rot=0, subplots=True)
        plt.savefig(heading + '.png')
        return plt.show()
    if variable == "Growth Rate":
        gplot.plot.bar(rot=0, subplots=True)
        plt.savefig(heading + '.png')
        return plt.show()


