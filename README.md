# Airbiome_Project
This reposatory contains the bioinformatics tools to analyse the Airbiome in Medellín.
The used workflows are using either [nextflow](https://www.nextflow.io/) with containers (Singularity, Docker,..) to ensure reproducibility.
It also contains bash and pyton scripts which do not need more than a few preinstalled packages to run.
## Requirements
-Python3 with packages numpy and pandas \
-Nextflow version >= 20.10 but <=  22.10 \
-Java v11+ \
-Singularity, Docker, Podman, Shifter or Charliecloud 
## Reads preprocessing and taxonomic profiling 
This project uses [nf-co.re/taxprofiler](https://nf-co.re/taxprofiler/1.0.0) for the reads preprocessing, taxonomic profiling and krona plots.  
This taxonomic pipeline  uses Nextflow. It can use a variety of different 
containers such as Singularity, Docker, Podman, Shifter or Charliecloud. As an input it accepts single or 
paired end fastq or even single end fasta files. The pipeline starts with adapter trimming and filtering. 
It does then a taxonomic classification with kraken2 and/or MetaPhlAn3. It uses then the output to create krona plots. 
For every step it can be chosen wheter it is made. For more detailed information, please click [here](https://nf-co.re/taxprofiler/1.0.0). \
Databeses necessary for kraken2 or metaphlan3 should be downloaded [here](https://benlangmead.github.io/aws-indexes/k2) or with the following command, respectively: 

```
wget https://zenodo.org/record/4629921/files/metaphlan_databases.tar.gz 
tar -xzf metaphlan_databases.tar.gz
```

Before you can start using taxoprofiler change sample.csv and database.csv. 
In order to do a txonomic profiling with kraken2 and metaphlan3 and produce krona plots, run the following command:

```
NXF_VER=22.10.1 nextflow run nf-core/taxprofiler --input sample.csv --databases database.csv --outdir output_test -profile docker --run_metaphlan3 --run_kraken2 --run_krona --max_memory '24 GB' --max_cpus 6
```

Tip: You do not have to type NXF_VER=22.10.1 if your nextflow version is between 20.10 and 22.10 

However, there are are a great number of other possibilities, how to use nf-core/taxoprofiler.
In order to calculate different alpha diversity indices with the metaphlan3 taxonimic profiling output, run the following command:


```
bash execute_alpha_div.sh

```
The script execute_alpha_div calls alpha_div.nf which in turn uses qiime2. Of course, you do not have to install qiime because the nextflow pipeline uses a docker image!
The alpha diversity output can then be used to plot boxplots and compare between sample. The script alpha_ttest.py uses a pairwise t-test. However, the test can be easily changed in the script. To run the script, type:


```
pyton alpha_ttest.py

```
Tip: Instead of ***python*** you can also use ```python3```.

