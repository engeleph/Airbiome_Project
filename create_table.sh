#!/bin/bash

otu="OTU"

#mkdir -p output_test/beta_diversity
#create first column with OTU names
dir=$PWD/output_test/kraken2/db2
sample_1="minigut_sample2"
mkdir -p output_test/beta_diversity/
echo $otu>>output_test/beta_diversity/table.txt
cat ${dir}/1_se_SRR12170646_db2.kraken2.kraken2.report.txt | awk '$4 == "S" {print $6,$7,$8}' >> output_test/beta_diversity/table.txt

for filename in ${dir}/*report.txt
do
        sample=$(basename ${filename})
	sample=${sample%_db2.kraken2.kraken2.report.txt}
        echo $otu$'\t'${sample}>>sample.txt
        cat ${filename} | awk '$4 == "S" {print $6,$7,$8 "\t" $2}'>> sample.txt
       	python create_table.py --sample ${sample}
        rm -r sample.txt
done

