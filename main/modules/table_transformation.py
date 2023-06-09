#!/bin/python

#This script uses log2(x+1) to account for "outliers"/ huge differences in otu counts. Otherwise otu with high counts have a huge influence on analysis

import sys
import os
import pandas as pd
import numpy as np


path_input="output_test"
number_groups=len(next(os.walk(path_input))[1])

for group in range(1,number_groups):
    df=pd.read_csv('output_test/group_{}/counting_table/table.txt'.format(group), sep='\t', index_col=0, header=0)
    
    df2=np.log2(df+1)
    
    df2.to_csv('output_test/group_{}/counting_table/normalized_table.txt'.format(group), index=True, sep ='\t')

