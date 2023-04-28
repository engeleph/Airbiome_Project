#calculate beta-diversity with wieghted jaccard similarity
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--group1", help="Number of group 1")
parser.add_argument("--group2", help="Number of group 2")
args = parser.parse_args()

group1=args.group1
group2=args.group2

df1=pd.read_csv('output_test/group_{}/beta_diversity/table.txt'.format(group1), sep='\t', index_col=0) #load df with samples and number of reads per OTU (genus level)
df2=pd.read_csv('output_test/group_{}/beta_diversity/table.txt'.format(group2), sep='\t', index_col=0)
df=df1.merge(df2, how='outer', on='OTU')
otu=df.index                                        #create array containg genus names
df = df.fillna(0)                                            #invert df so that the columns are otus and rows are samples

m=len(df1.columns)
n=len(df2.columns)
df4=pd.DataFrame({'samples':[],'weighted jaccard':[],'Bray Curtis distance':[], 'Euclidean Distance':[]})
#colors = []
for i in range (m):
    for j in range (n):
        col_name1=df1.columns[i]                         #first sample name
        col_name2=df2.columns[j]                #second sample name

        col_combined='{}-{}'.format(col_name1,col_name2)    #combine sample names
        samples_df=pd.DataFrame({'x':df[col_name1], 'y':df[col_name2]})
        
        #union=np.sum(df.loc[df[col_name2]!=0][col_name1]!=0)       #OTUs of samples which have reads in both samples
        #inter=union+np.sum(df.loc[df[col_name2]!=0][col_name1]==0)+np.sum(df.loc[df[col_name1]!=0][col_name2]==0)      #OTUs of samples which have reads in either samples        
        counter_bc=np.sum(abs(samples_df["x"]-samples_df["y"]))
        denominator_bc=np.sum(samples_df["x"]+samples_df["y"])
        bc=round(counter_bc/denominator_bc,5)
        eu_d=round(np.sqrt(np.sum((samples_df["x"]-samples_df["y"])**2)),3)
        minimum=np.sum(samples_df.min(axis=1))
        maximum=np.sum(samples_df.max(axis=1))
        #jaccard=round(union/inter,5)                    #calculate jaccard index
        jaccard=round(minimum/maximum,5)                 #calculate weighted jaccard index
        jaccard_div=1-jaccard
        df3=pd.DataFrame({'samples':[col_combined],'weighted jaccard':[jaccard_div],'Bray Curtis distance':[bc], 'Euclidean Distance':[eu_d]})    #include combined sample names and their jaccard index
        df4=df4.append(df3, ignore_index=True)

path="output_analysis/beta_diversities/betadiversity_groups_{}_{}".format(group1,group2)
isExist = os.path.exists(path)
if not isExist:
   os.makedirs(path)
#change to output directory
os.chdir(path)

df4.to_csv('beta_metrices.txt', header=True, sep ='\t')


'''
#os.chdir('/cluster/project/grlab/projects/metasub/results/metasub_rna/results')
plt.rcParams["figure.figsize"] = (20,10)
plt.bar(df2['samples'],df2['jaccard'], color=colors)
plt.title("Jaccard index between samples")
plt.xticks(rotation=90)
plt.xlabel("samples")                                       
plt.ylabel("Jaccard index")
plt.savefig('results/batch_effect/jaccard_index.png')
'''
