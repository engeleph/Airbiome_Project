#!/bin/bash

count=$(ls $PWD/output_test/ | wc -l)
echo "$count"

otu="OTU"

echo "Create counting table"

for i in `seq 1 $count`
do

        #create first column with OTU names
        dir=$PWD/output_test/group_${i}

        mkdir -p ${dir}/counting_table/
        echo $otu>${dir}/counting_table/table.txt
        
        touch ${dir}/counting_table/table.txt

        for filename in ${dir}/bracken/db1/*
        do
                sample=$(basename ${filename})
                sample=${sample%_db1.bracken.tsv}
                sample=${sample##*se_}
                #echo "Adding sample ${sample} to counting table of group ${i} ... "
                echo $otu$'\t'${sample}>>sample.txt
                cat ${filename} | awk '$4 == "S" {print $1,$2 "\t" $7}'>> sample.txt
                cat ${filename} | awk '$5 == "S" {print $1,$2,$3 "\t" $8}'>> sample.txt
                python create_table.py --group ${i}
                rm -r sample.txt
        done
done

echo "Counting table created!"

#calculate alpha diversities
echo "Calculate alpha diversites"

#python3 alpha_diversity.py 

#create barplot of alpha diversity in each group
echo "Bar plot and pairwise ttest of alpha diversities"

python3 alpha_ttest.py

echo"Calculate beta diverity indices"

for i in `seq 1 $((count-1))`
do
        for j in `seq $((i+1)) $count`
        do
                python3 beta_diversity.py --group1 $i --group2 $j
                cat output_analysis/beta_diversities/betadiversity_groups_${i}_${j}/beta_metrices.txt | awk '{print $3}' > output_analysis/beta_diversities/betadiversity_groups_${i}_${j}/jaccard_values.csv
        done
done

echo "Bar plot and pairwise ttest of alpha diversities"

python3 beta_ttest.py
