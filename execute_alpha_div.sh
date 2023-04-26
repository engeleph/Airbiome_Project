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
	done
done
