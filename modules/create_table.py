import sys
import os
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='sample name')
parser.add_argument("--group", required=True, help="Group Number")
args = parser.parse_args()
group=args.group

#load df from current sample counts
df=pd.read_csv('sample.txt', sep='\t', header=0)    

#load df from merged sample counts
df2=pd.read_csv('output_test/group_{}/counting_table/table.txt'.format(group), sep='\t', header=0)

#join both df based on OTU names 
df2=df2.merge(df, how='outer', on='OTU')        

#all NA values are replaced by 0 (no counts)
df2 = df2.fillna(0)             

#np.savetxt(r'/home/philipp/Documents/Airbiome_Project/nxf-kraken2/table.txt', df2)  #fmt='%d'
df2.to_csv('output_test/group_{}/counting_table/table.txt'.format(group),sep='\t',index=False)
