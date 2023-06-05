#script to calculate shannon alpha diversitiy
import sys
import os
import pandas as pd
import numpy as np



path_input="output_test"
number_groups=len(next(os.walk(path_input))[1])

for group in range(1,number_groups):
    df=pd.read_csv('output_test/group_{}/counting_table/normalized_table.txt'.format(group), sep='\t', index_col=0)
    
    #calculate shannon diversity
    n=len(df)
    m=len(df.columns)
    df2=pd.DataFrame({'sample':[],'shannon':[],'simpson':[],'chao1':[]})

    for i in range(m):
        col_name=df.columns[i]
        col_sum=df[col_name].sum()
        col_sample=df[col_name]
        shannon=0
        simpson=0
        n_n=0
        N=0
        singleton=0
        doubleton=0
        s_obs=0
        for j in range(n):
                if col_sample[j]>0:
                        shannon=shannon+((col_sample[j]/col_sum)*np.log(col_sample[j]/col_sum))
                        n_n = n_n + col_sample[j]*(col_sample[j]-1)                #calculates  sum of all n*(n-1) for simpsonsdiversity
                        N=N+col_sample[j]    #calculates N
                        s_obs+=1
                        if col_sample[j]==1:
                            singleton+=1
                        elif col_sample[j]==2:
                            doubleton+=1
    
        chao1 = s_obs+((singleton)**2/2*doubleton)
        shannon=(-1)*shannon                 
        shannon="{:.4f}".format(shannon)

        N_N=N*(N-1)                   #calculates N*(N-1)
        simpson=1-(n_n/N_N)
        simpson="{:.4f}".format(simpson)
        df3=pd.DataFrame({'sample':[col_name],'shannon':[shannon],'simpson':[simpson], 'chao1':[chao1]})
        df2=df2.append(df3, ignore_index=True)

    path_output="output_test/group_{}/alpha_diversity/".format(group)
    isExist = os.path.exists(path_output)
    if not isExist:
        os.makedirs(path_output)

    df2.to_csv('output_test/group_{}/alpha_diversity/alpha_diversities.txt'.format(group), header=True, sep ='\t')

