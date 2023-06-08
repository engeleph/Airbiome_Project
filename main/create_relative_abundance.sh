#!/bin/bash

count=$(ls $PWD/output_test/ | wc -l)

phylum="Phylum"


for i in `seq 1 $count`
do

        #create first column with OTU names
        dir=$PWD/output_test/group_${i}

        mkdir -p ${dir}/counting_table/
        echo $otu>${dir}/counting_table/table.txt

        #touch ${dir}/beta_diversity/phyla_table.txt
	echo "$phylum"> ${dir}/counting_table/abundance_table.txt

        for filename in ${dir}/kraken2/db1/*kraken2.report.txt
        do
                sample=$(basename ${filename})
                sample=${sample%_db1.bracken.kraken2.report.txt}
                sample=${sample##*se_}
                #echo "Adding sample ${sample} to counting table of group ${i} ... "
                echo ${phylum}$'\t'${sample}>sample.txt
		classified=$(cat ${filename} | awk '$4 == "R" {print $2}')
                cat ${filename} | awk '$4 == "P" {print $6 "\t" $2}'>> sample.txt
		cat sample.txt | awk -v c=$classified '{ print $1 "\t" $2/c }' >> sample2.txt
                python3 modules/create_relative_abundance.py --group ${i} --sample ${sample}
                rm -r sample.txt
		rm -r sample2.txt
        done
done

echo "Create relative abundance plot"

python3 modules/plot_relative_abundance.py
