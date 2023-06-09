import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from statannot import add_stat_annotation
import os
import sys
sys.path.append('conf')
from config import beta_index, beta_test


#this part calculate the number of subdirectories in output_test which is equal to the number of groups

path="output_test"

number_groups=len(next(os.walk(path))[1])       

#the following steps work if you have at least 2 groupwise comparisons, which makes sense for pairwise comparison
df=pd.read_csv("output_analysis/beta_diversities/betadiversity_groups_1_2/beta_metrices.txt", sep='\t', header=0)  #first dataframe to start with

df=df[[beta_index]]
df["group_pair"]="1_2"    #belongs to group 0
order=[]
x=0            #x is used to calculate total number of pairwise beta diversity
#concat all data frames to 1 big cone
for i in range(1,(number_groups-1)):
    for j in range((i+1),number_groups):
        df2=pd.read_csv("output_analysis/beta_diversities/betadiversity_groups_{}_{}/beta_metrices.txt".format(i,j), sep='\t', header=0)
        df2=df2[[beta_index]]
        df2["group_pair"]="{}_{}".format(i,j)
        df=pd.concat([df,df2])
        order.append("{}_{}".format(i,j))
        x=x+1    

#creates pairs and order of samples of pairwise ttests
pairs=[]
for i in range((x-1)):
    for j in range((i+1),x):
        element=(order[i],order[j])
        pairs.append(element)

x="group_pair"
y=beta_index

#create seaborn boxplot with statistics
ax = sns.boxplot(data=df, x=x, y=y, order=order)
add_stat_annotation(ax, data=df, x=x, y=y, order=order, box_pairs=pairs, test=beta_test, text_format='star', loc='outside', verbose=2)  #test='Mann-Whitney'
plt.legend(loc='upper left', bbox_to_anchor=(1.03, 1))
plt.ylabel(beta_index)
plt.axis("tight")

#checks if output path output_analysis exists and creates it if not
path_output="output_analysis/plots"
isExist = os.path.exists(path_output)
if not isExist:
   os.makedirs(path_output)
#change to output directory
os.chdir(path_output)
#save plot
plt.savefig("boxplot_beta_diversity.jpg")
