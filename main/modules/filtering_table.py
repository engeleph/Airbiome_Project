#!/bin/python

#This script filters the individual tables so that average counts in each group with <=3 counts are checked for each samples. If less than 50% of the samples are more than 0, this OTO is set to 0 for all samples.

import sys
import os
import pandas as pd
import numpy as np
sys.path.append('conf')
from config import filter_size, filter_proportion


path_input="output_test"
number_groups=len(next(os.walk(path_input))[1])

for group in range(1,2):
    #load OTU table
    df=pd.read_csv('output_test/group_{}/counting_table/table.txt'.format(group), sep='\t', index_col=0, header=0)

    samples = df.columns
    
    n=len(df)
    m=len(df.columns)

    df["mean"]=df.mean(axis=1)
    df["count"]=(df[samples] == 0).astype(int).sum(axis=1) 

    df2=df[samples].loc[(df["mean"]>filter_size) | (df["count"]<=filter_proportion*m)]
    
    df2.to_csv('output_test/group_{}/counting_table/table.txt'.format(group), index=True, sep ='\t')

    #calculate mean of otu table
