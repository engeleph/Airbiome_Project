import sys
import os
import pandas as pd
import numpy as np

path_input="output_test"
number_groups=len(next(os.walk(path_input))[1])

#load df from current sample counts
df=pd.read_csv('output_test/group_1/counting_table/normalized_table.txt', sep='\t', header=0)
#print(df)

for group in range(2,number_groups):

    #load df from merged sample counts
    df2=pd.read_csv('output_test/group_{}/counting_table/normalized_table.txt'.format(group), sep='\t', header=0)
    #print(df2)
    #join both df based on OTU names 
    df=df2.merge(df, how='outer', on='OTU')
    #print(df2)
#all NA values are replaced by 0 (no counts)
df = df.fillna(0)
#print(df)

path_output="output_analysis/total_counting_table/"
isExist = os.path.exists(path_output)
if not isExist:
    os.makedirs(path_output)
#np.savetxt(r'/home/philipp/Documents/Airbiome_Project/nxf-kraken2/table.txt', df2)  #fmt='%d'
df.to_csv('output_analysis/total_counting_table/table.txt'.format(group),sep='\t',index=False)

