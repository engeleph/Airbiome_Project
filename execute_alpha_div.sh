#!/bin/bash
count=$(ls $PWD/output_test/ | wc -l)

for i in `seq 1 $count`
do
	for file in ./output_test/group_${i}/metaphlan3/db4/*_db4.metaphlan3.biom
	do
		in=$(basename $file)
		sampleName=${in%_db4.metaphlan3.biom}
		sample=${sampleName##*se_}
		NXF_VER=21.10.6 nextflow run alpha_div.nf --sampleName "$sampleName" --sample "$sample" --basedir "$PWD" --group "$i"  -with-docker qiime2/core
		tsv=$PWD/output_test/group_${i}/alpha_diversity/${sample}_alpha_diversity.tsv
		if [ -f "$tsv" ]; then
    			rm -rf $tsv
		fi
	
		cat $tsv | awk '$1=="shannon" {print $2}' >> $PWD/output_test/group_${i}/alpha_diversity/alpha_values.csv
	done
done
