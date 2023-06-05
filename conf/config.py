#!/bin/python

###This file contains all the choosable variables/configurations
### Choose them before you start running the scripts. as they are used in different scripts during the pipeline

#filter configuration: if the average OTU count in one group is smaller than the filter size and proportion of 0 is also bigger than the filter proportion, this OTU is set to 0 in this group
filter_size=3          
filter_proportion=0.5

#alpha diversity configurations
alpha_index="shannon"    #choose with which alpha diversity index you want to create a boxplot, options: [shannon,simpson]
alpha_test="t-test_ind"   #choose which test you want to compare alpha diversities in boxplot, options: [t-test_ind, t-test_welch, t-test_paired, Mann-Whitney, Mann-Whitney-gt, Mann-Whitney-ls, Levene, Wilcoxon, Kruskal]

#beta diversity configurations
beta_index="weighted jaccard"   # choose with wich beta diversity index you want to create a boxplot, options: [weighted jaccard, Bray Curtis distance, Euclidean Distance]
beta_test="t-test_ind"   #choose which test you want to compare alpha diversities in boxplot, options: [t-test_ind, t-test_welch, t-test_paired, Mann-Whitney, Mann-Whitney-gt, Mann-Whitney-ls, Levene, Wilcoxon, Kruskal]


#plot relative abundance
number_otus=8             #not more than the 10 most abundant OTUs (+ others) can be plot

