#!/bin/bash

count=$(ls $PWD/output_test/ | wc -l)

for i in `seq 1 $((count-1))`
do
	for j in `seq $((i+1)) $count`
        do
                python3 beta_diversity.py --group1 $i --group2 $j
		cat output_analysis/beta_diversities/betadiversity_groups_${i}_${j}/beta_metrices.txt | awk '{print $3}' > output_analysis/beta_diversities/betadiversity_groups_${i}_${j}/jaccard_values.csv
        done
done

