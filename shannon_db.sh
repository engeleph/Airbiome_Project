#!/bin/bash

count=$(ls $PWD/output_test | wc -l)

for z in `seq 1 $count`
do
        for file in $PWD/output_test/group_${z}/alpha_diversity/*.tsv
        do
                cat $file | awk '$1=="shannon" {print $2}' >> $PWD/output_test/group_${z}/alpha_diversity/alpha_values.csv
        done
done
