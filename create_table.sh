#!/bin/bash

count=$(ls $PWD/output_test/ | wc -l)

otu="OTU"


for i in `seq 1 $count`
do

	#create first column with OTU names
	dir=$PWD/output_test/group_${i}
	if [ -f "$dir/beta_diversity/table.txt" ]; then
            rm -rf $dir/beta_diversity/table.txt
        fi

	mkdir -p ${dir}/beta_diversity/
	echo $otu>>${dir}/beta_diversity/table.txt
	#cat ${dir}/kraken2/db2/1_se_SRR12170646_db2.kraken2.kraken2.report.txt | awk '$4 == "S" {print $6,$7,$8}' >> ${dir}/beta_diversity/table.txt
	touch ${dir}/beta_diversity/table.txt

	for filename in ${dir}/bracken/db1/*
	do
		sample=$(basename ${filename})
		sample=${sample%_db1.bracken.tsv}
		sample=${sample##*se_}
		echo "Adding sample ${sample} to counting table of group ${i} ... "
        	echo $otu$'\t'${sample}>>sample.txt
        	cat ${filename} | awk '$4 == "S" {print $1,$2 "\t" $7}'>> sample.txt
       		python create_table.py --group ${i}
        	rm -r sample.txt
	done
done

echo "Done!"
