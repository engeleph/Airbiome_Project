#!/bin/bash
# this script uses metaphlan3 output to create counting table on species level
datadir=/home/philipp/Documents/Airbiome_Project/taxprofiler/Airbiome_Project
otu="OTU"
#create first column with OTU names
dir=${datadir}/output_test/metaphlan3/db4
sample_1="sample1"
echo $otu>>${datadir}/table.txt
#cat ${dir}/1_se_SRR12170646_db4.metaphlan3_profile.txt | awk '$1 ~ /s__/ {print $3}' >> ${datadir}/table.txt
cat ${dir}/1_se_SRR12170646_db4.metaphlan3_profile.txt | awk  'match($0,/s__[^ ]*/,arr){ print arr[0]}' | awk -F '\t' '{print $1}' >> ${datadir}/table.txt

for filename in ${dir}/*metaphlan3_profile.txt
do
        sample=$(basename ${filename})
        echo $otu$'\t'${sample} >> ${datadir}/sample.txt
        cat ${filename} | awk 'match($0,/s__[^ ]*/,arr){ print arr[0]}' | awk -F '\t' '{print $1 "\t" $3}'>> ${datadir}/sample.txt
        python create_table.py --sample ${sample}
        rm -r ${datadir}/sample.txt
done

