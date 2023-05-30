import numpy as np
from sklearn.decomposition import PCA,IncrementalPCA
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import matplotlib.pyplot as plt

#function to normalize data
def dataNormalisation(X):
    mean=X.mean(axis=0)
    std=np.std(X, axis=0)
    X_std = (X-mean)/(std+0.00001)
    return X_std


##create table which contains samples with otu counts (genus level) and the corresponding information (sampler, location, etc)
df=pd.read_csv('output_analysis/total_counting_table/table.txt', sep='\t', index_col=0)  #load table with genus counts
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


##create PCA with 2 PCs
df_rep = df[otu]
df_rep[df_rep.isnull()]=0
df[otu]=df_rep
df[otu]=dataNormalisation(df[otu]) #normalize otu reads
pca = PCA(n_components=2)
components=pca.fit_transform(df[otu])

##create scatter plot with samplers in different colors
path_output="output_analysis/batch_effect/"
isExist = os.path.exists(path_output)
if not isExist:
    os.makedirs(path_output)

fig = px.scatter(components, x=0,y=1, color=df["group"], title="PCA with replicates differently colored", labels={0:"PCA 1",1:"PCA 2"})
fig.write_image('output_analysis/batch_effect/PCA.png')
