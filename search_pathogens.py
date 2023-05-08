import os
import pandas as pd
import numpy as np

path_input="output_test"
number_groups=len(next(os.walk(path_input))[1])
pathogens=["Streptococcus pneumoniae", "Aspergillus fumigatus", "human adenovirus C"]

def search_pathogen(file_path, word, pathogen):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            pathogen="True"
        else:
            pathogen="False"

df=pd.DataFrame({'group':[],'Streptococcus pneumoniae':[],'Aspergillus fumigatus':[],'Human adenovirus C':[]})

for group in range(3,(number_groups+1)):
    streptococcus="False"
    aspergillus="False"
    adenovirus="False"
    #df2=pd.read_csv("output_test/group_{}/beta_diversity/phyla_table.txt".format(group), sep='\t', header=0)
    
    search_pathogen("output_test/group_{}/beta_diversity/phyla_table.txt".format(group), pathogens[0], streptococcus)
    search_pathogen("output_test/group_{}/beta_diversity/phyla_table.txt".format(group), pathogens[1], aspergillus)
    search_pathogen("output_test/group_{}/beta_diversity/phyla_table.txt".format(group), pathogens[2], adenovirus)
    
    df2=pd.DataFrame({'group':[group],'Streptococcus pneumoniae':[streptococcus],'Aspergillus fumigatus':[aspergillus],'Human adenovirus C':[adenovirus]})

    df=df.append(df2, ignore_index=True)

#checks if output path output_analysis exists and creates it if not
path_output="output_analysis/pathogens" 
isExist = os.path.exists(path_output)
if not isExist:
   os.makedirs(path_output)
#change to output directory
os.chdir(path_output)


df.to_csv('pathogens.txt', header=True, sep ='\t')
        

