import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import CCA
from sklearn.manifold import MDS # for MDS dimensionality reduction
import plotly.express as px # for data visualization

##create table which contains samples with otu counts (species level)
df=pd.read_csv('output_analysis/total_counting_table/table.txt', sep='\t', index_col=0, header=0)  #load table with species counts
otu=df.index                                        #create array containg genus names
df=df.T                                             #invert df so that the columns are otus and rows are samples

df["group"]=0
index=0
path_groups="output_test"
number_groups=len(next(os.walk(path_groups))[1])
for group in range(1,number_groups):
    path_samples="output_test/group_{}/kraken2/db1".format(group)
    #number_samples=len(next(os.walk(path_samples))[1])-1
    number_samples=0
    for path in os.scandir(path_samples):
        if path.is_file():
            number_samples += 1
    df["group"].iloc[index:(index+number_samples)]=group
    index=index+number_samples

### Step 1 - Configure MDS function, note we use default hyperparameter values for this example
model2d=MDS(n_components=2,
          metric=True,
          n_init=4,
          max_iter=300,
          verbose=0,
          eps=0.001,
          n_jobs=None,
          random_state=42,
          dissimilarity='euclidean')

### Step 2 - Fit the data and transform it, so we have 2 dimensions instead of 3
X_trans = model2d.fit_transform(df[otu])

### Step 3 - Print a few stats
print('The new shape of X: ',X_trans.shape)
print('No. of Iterations: ', model2d.n_iter_)
print('Stress: ', model2d.stress_)

#print(df)

# Create a scatter plot
fig = px.scatter(None, x=X_trans[:,0], y=X_trans[:,1], opacity=1, color=df["group"].apply(str),labels={"x":"x","y":"y","color":"Group"})

# Change chart background color
fig.update_layout(dict(plot_bgcolor = 'white'))

# Update axes lines
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',
                 zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey',
                 showline=True, linewidth=1, linecolor='black')

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',
                 zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey',
                 showline=True, linewidth=1, linecolor='black')

# Set figure title
fig.update_layout(title_text="MDS Transformation")

# Update marker size
fig.update_traces(marker=dict(size=5,
                             line=dict(color='black', width=0.2)))

#fig.show()
fig.write_image('output_analysis/batch_effect/MDS.png')

