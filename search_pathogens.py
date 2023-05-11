import os
import pandas as pd
import numpy as np

path_input="output_test"
number_groups=len(next(os.walk(path_input))[1])
#pathogens=["Streptococcus pneumoniae", "Aspergillus fumigatus", "human adenovirus C"]
pathogens=pd.read_csv("pathogens.txt", sep='\t', header=0) 
#pathogens["present"]="Unknown"
pathogens.set_index("pathogens",drop=True,inplace=True)

def search_pathogen(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            return "True"
        else:
            return "False"


for group in range(1,number_groups):
    pathogens["group_{}".format(group)]="Unknown"
    #df2=pd.read_csv("output_test/group_{}/beta_diversity/phyla_table.txt".format(group), sep='\t', header=0)
    for i in range(len(pathogens.index)):
        pathogens["group_{}".format(group)].loc[pathogens.index[i]]=search_pathogen("output_test/group_{}/counting_table/phyla_table.txt".format(group), pathogens.index[i])
    
print(pathogens)

#checks if output path output_analysis exists and creates it if not
path_output="output_analysis/pathogens" 
isExist = os.path.exists(path_output)
if not isExist:
   os.makedirs(path_output)
#change to output directory
os.chdir(path_output)


pathogens.to_csv('pathogens.txt', header=True, sep ='\t')

