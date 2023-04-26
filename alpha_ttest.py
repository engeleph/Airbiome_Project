import argparse
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from statannot import add_stat_annotation
import os

#this part calculate the number of subdirectories in output_test which is equal to the number of groups
path_input="output_test"
path_output="output_analysis"

number_groups=len(next(os.walk(path_input))[1])

#the following steps work if you have at least 2 groups, which makes sense for pairwise comparison
df=pd.read_csv("output_test/group_1/alpha_diversity/alpha_values.csv", sep='\t', header=None)  #first dataframe to start with
df["sample"]=1    #belongs to group 0

#concat all data frames to 1 big cone
for i in range(1,number_groups):
    x=i+1
    df2=pd.read_csv("output_test/group_{}/alpha_diversity/alpha_values.csv".format(x), sep='\t', header=None)
    df2["sample"]=x
    df=pd.concat([df,df2])
df=df.rename({0: 'shannon'}, axis=1)  # rename first column to shannon

#creates pairs and order of samples of pairwise ttests
pairs=[]
order=[1]
for i in range(1,number_groups):
    order.append((i+1))
    for j in range((i+1),(number_groups+1)):
        element=(i,j)
        pairs.append(element)

x="sample"
y="shannon"

#create seaborn boxplot with statistics
ax = sns.boxplot(data=df, x=x, y=y, order=order)
add_stat_annotation(ax, data=df, x=x, y=y, order=order, box_pairs=pairs, test='t-test_ind', text_format='star', loc='outside', verbose=2)  #test='Mann-Whitney'
plt.legend(loc='upper left', bbox_to_anchor=(1.03, 1))
plt.ylabel("Shannon Index")

#checks if output path output_analysis exists and creates it if not
isExist = os.path.exists(path_output)
if not isExist:
   os.makedirs(path_output)
#change to output directory
os.chdir(path_output)
#save plot
plt.savefig("boxplot.jpg")
