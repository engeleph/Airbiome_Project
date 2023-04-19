import sys
import os
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='sample name')
parser.add_argument("--sample", required=True, help="Path to input directory containing file EGC200_TRAIN.txt")
args = parser.parse_args()
sample=args.sample

#os.chdir("/home/philipp/Documents/Airbiome_Project/taxprofiler/Airbiome_Project")

df=pd.read_csv('sample.txt', sep='\t', header=0)

df2=pd.read_csv('table.txt', sep='\t', header=0)

df2=df2.merge(df, how='outer', on='OTU')

df2 = df2.fillna(0)

print(df2)

#np.savetxt(r'/home/philipp/Documents/Airbiome_Project/nxf-kraken2/table.txt', df2)  #fmt='%d'
df2.to_csv('table.txt',sep='\t',index=False)
