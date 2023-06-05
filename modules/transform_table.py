import pandas as pd

df=pd.read_csv('output_analysis/total_counting_table/table.txt', sep='\t', index_col=0, header=0)  #load table with species counts
otu=df.index                                        #create array containg genus names
df=df.T
df.to_csv('output_analysis/total_counting_table/t_table.txt', header=True, sep ='\t')
