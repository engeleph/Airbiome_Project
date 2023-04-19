#!/bin/bash

datadir=/home/philipp/Documents/Airbiome_Project/nxf-kraken2
otu="OTU"

#create first column with OTU names
dir=${datadir}/results-kraken2/samples
sample_1="minigut_sample2"
echo $otu>>${datadir}/table.txt
cat ${dir}/minigut_sample1_kraken2.report | awk '$4 == "S" {print $6,$7}' >> ${datadir}/table.txt

for filename in ${dir}/*kraken2.report
do
        sample=$(basename ${filename})
        echo $otu$'\t'${sample}>>${datadir}/sample.txt
        cat ${filename} | awk '$4 == "S" {print $6,$7 "\t" $2}'>> ${datadir}/sample.txt
       	python create_table.py --sample ${sample}
        rm -r ${datadir}/sample.txt
done

