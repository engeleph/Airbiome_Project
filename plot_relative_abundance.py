import argparse
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from statannot import add_stat_annotation
import os
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.core.properties import value
from bokeh.palettes import Spectral
import itertools


#this part calculate the number of subdirectories in output_test which is equal to the number of groups
path_input="output_test"
path_output="output_analysis/plots"

number_groups=len(next(os.walk(path_input))[1])

samples=[]
#the following steps work if you have at least 2 groups, which makes sense for pairwise comparison
df=pd.read_csv("output_test/group_3/beta_diversity/phyla_table.txt", sep='\t', header=0)  #first dataframe to start with
samples.append((len(df.columns)-1))

#concat all data frames to 1 big cone
for i in range(3,number_groups):
    x=i+1
    df2=pd.read_csv("output_test/group_{}/beta_diversity/phyla_table.txt".format(x), sep='\t', header=0)
    df=df.merge(df2, how='outer', on='Phylum')
    samples.append(len(df2.columns)-1)
df = df.fillna(0)
df.reset_index(drop=True, inplace=True)

df["mean"]=df.mean(axis=1)

df=df.sort_values('mean', ascending=False)
df=df.head(10)
#df=df.iloc[0:10,:]


#create row for abundance of others (than the 10 most abundant species)
others=df[:].sum(axis=0)
others=1-others[1:]          
others=pd.concat([pd.Series(['others']),others])
others=others.rename({0: "Phylum"}) 

#join main dataframe with others
df=df.transpose()
df3=pd.concat([df, others], axis=1)
df3=df3.transpose()

#creates dataframe with average relative abundance per group
x=1
df4=pd.DataFrame(df3["Phylum"])
for i in range(0,2):
    y=i+1
    end=x+samples[i]
    df4["group_{}".format(y)]=df3.iloc[:,x:end].mean(axis=1)
    x=end


output_file("output_analysis/plots/stacked.html")

df2=pd.DataFrame([[0]*df4.shape[1]],columns=df4.columns)



df4.set_index("Phylum", inplace=True)
samples = df4.columns.values
organisms = df4.index.values
#organisms = np.delete(organisms,0)
# You have two rows with 'uncultured' data. I added these together.
# This may or may not be what you want.
df4 = df4.groupby('Phylum')[samples].transform('sum')
# create a color iterator
# See https://stackoverflow.com/q/39839409/50065
# choose an appropriate pallete from
# https://docs.bokeh.org/en/latest/docs/reference/palettes.html
# if you have a large number of organisms
color_iter = itertools.cycle(Spectral[11])    
colors = [next(color_iter) for organism in organisms]

# create a ColumnDataSource
data = {'samples': list(samples)}
for organism in organisms:
    data[organism] = list(df4.loc[organism])
source = ColumnDataSource(data=data)

# create our plot
p = figure(x_range=samples, plot_height=350, title="Species abundance",
           toolbar_location=None, tools="")

p.vbar_stack(organisms, x='samples', width=0.9, source=source,
             legend=[value(x) for x in organisms], color=colors)

p.xaxis.axis_label = 'Sample'
p.yaxis.axis_label = 'Relative Abundance'
p.legend.location = "top_right"
p.legend.orientation = "vertical"
# Position the legend outside the plot area
# https://stackoverflow.com/questions/48240867/how-can-i-make-legend-outside-plot-area-with-stacked-bar
new_legend = p.legend[0]

p.add_layout(new_legend, 'right')
#savefig("boxplot_relative_abundance.jpg")
show(p)

