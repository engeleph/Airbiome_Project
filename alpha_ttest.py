import argparse
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from statannot import add_stat_annotation

#parser = argparse.ArgumentParser(description='sample1 name')
#parser.add_argument("--sample1", required=True, help="shannon values of first db")
#parser.add_argument("--sample2", required=True, help="shannon values of second db")
#args = parser.parse_args()
#sample1=args.sample1
#sample2=args.sample2

df=pd.read_csv("output_test/alpha_diversity/alpha_values_1.csv", sep='\t', header=None)
df2=pd.read_csv("output_test/alpha_diversity/alpha_values_2.csv", sep='\t', header=None)

df["sample"]=1
df2["sample"]=2

df_con=pd.concat([df,df2])
df_con=df_con.rename({0: 'shannon'}, axis=1)
print(df_con)

x="sample"
y="shannon"
order=[1,2]

ax = sns.boxplot(data=df_con, x=x, y=y, order=order)
add_stat_annotation(ax, data=df_con, x=x, y=y, order=order, box_pairs=[(1, 2)], test='t-test_ind', text_format='star', loc='outside', verbose=2)  #test='Mann-Whitney'
plt.legend(loc='upper left', bbox_to_anchor=(1.03, 1))
plt.ylabel("Shannon Index")

plt.savefig("boxplot.jpg")
