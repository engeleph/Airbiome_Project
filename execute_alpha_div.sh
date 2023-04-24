#!/bin/bash

for file in ./output_test/metaphlan3/db4/*_db4.metaphlan3.biom
do
	in=$(basename $file)
	sample=${in%_db4.metaphlan3.biom}
	NXF_VER=21.10.6 nextflow run alpha_div.nf --sampleName "$sample" --basedir "$PWD"  -with-docker qiime2/core
done
