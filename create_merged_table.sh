#!/bin/bash

exist_here=0

for file in output_test/alpha_diversity/*_abundance_table.qza
do
    if [ ! -f "${PWD}/output_test/alpha_diversity/merged_table.qza" ]; then
	cat $file > output_test/alpha_diversity/merged_table.qza
        echo "$file"

    elif [ "$exist_here" -eq "1" ]; then
	echo "$file"
	sample=$(basename $file)
        NXF_VER=21.10.6 nextflow run beta_div.nf --new $sample --basedir $PWD  -with-docker qiime2/core
    fi
    exist_here=1
done
