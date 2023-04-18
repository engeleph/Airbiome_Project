#script to calculate shannon alpha diversitiy
import sys
import os
import pandas as pd
import numpy as np

os.chdir("/home/philipp/Documents/Airbiome_Project/nxf-kraken2")

df=pd.read_csv('table.txt', sep='\t', index_col=0)

#calculate shannon diversity
n=len(df)
m=len(df.columns)
df2=pd.DataFrame({'sample':[],'shannon':[],'simpson':[]})

for i in range(m):
        col_name=df.columns[i]
        col_sum=df[col_name].sum()
        col_sample=df[col_name]
        shannon=0
        simpson=0
        n_n=0
        N=0
        for j in range(n):
                if col_sample[j]>0:
                        shannon=shannon+((col_sample[j]/col_sum)*np.log(col_sample[j]/col_sum))
                        n_n = n_n + col_sample[j]*(col_sample[j]-1)                #calculates  sum of all n*(n-1) for simpsonsdiversity
                        N=N+col_sample[j]                                          #calculates N
        shannon=(-1)*shannon                 
        shannon="{:.4f}".format(shannon)

        N_N=N*(N-1)                   #calculates N*(N-1)
        simpson=1-(n_n/N_N)
        simpson="{:.4f}".format(simpson)
        df3=pd.DataFrame({'sample':[col_name],'shannon':[shannon],'simpson':[simpson]})
        df2=df2.append(df3, ignore_index=True)

df2.to_csv('alpha_diversity.txt', header=True, sep ='\t')

