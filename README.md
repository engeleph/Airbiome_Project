# Airbiome_Project
This reposatory contains the bioinformatics tools to analyse the Airbiome in Medellín.
The used workflows are using either [nextflow](https://www.nextflow.io/) with containers (Singularity, Docker,..) to ensure reproducibility.
It also contains bash and pyton scripts which do not need more than a few preinstalled packages to run.
## Requirements
-Python3 \
-Nextflow version >= 20.10 but <=  22.10 \
-Java v11+ \
-Docker 
## Documentation
This project uses [nf-co.re/taxprofiler](https://nf-co.re/taxprofiler/1.0.0) for the reads preprocessing, taxonomic profiling and krona plots.  
The taxonomic pipeline uses Nextflow. It can use a variety of different 
containers such as Singularity, Docker, Podman, Shifter or Charliecloud. As an input it accepts single or 
paired end fastq or even single end fasta files. The pipeline starts with adapter trimming and filtering. 
It does then a taxonomic classification with kraken2 and/or MetaPhlAn3. It uses then the output to create krona plots. 
For every step it can be chosen wheter it is made. For more detailed information, please click [here](https://nf-co.re/taxprofiler/1.0.0). \
However, before we start with the analysis of the metagenomic samles we have to install a few python packages. All the necessay packages can be found in the script ```python_packages.sh```. These packages can be installed manually or simply by running:

```
bash python_packages.sh
```

Databeses necessary for kraken2 and metaphlan3 should be downloaded [here](https://benlangmead.github.io/aws-indexes/k2) and with the following command, respectively: 

```
wget https://zenodo.org/record/4629921/files/metaphlan_databases.tar.gz 
tar -xzf metaphlan_databases.tar.gz
```
Tip: Different versions of metaphlan3 databases can also be downloaded [here](http://cmprod1.cibio.unitn.it/biobakery3/metaphlan_databases/)

Before you can start using taxoprofiler change sample_{NUMBER}.csv and database.csv. Every group (month/PM size/ ...) needs an own sample_{NUMBER}.csv table! In order to do a txonomic profiling with kraken2 and metaphlan3 and produce krona plots, run the following command:

```
NXF_VER=22.10.1 nextflow run nf-core/taxprofiler --input conf/sample_{NUMBER}.csv --databases conf/database.csv --outdir output_test/group_{NUMBER} -profile docker --run_kraken2 --run_bracken --max_memory '24 GB' --max_cpus 6
```
Tip 1: You can also create Krona plots (```--run_krona```) or do a txonomic classification with metaphlan3 (```--run_metaphlan3```). \
Tip 2: You do not have to type NXF_VER=22.10.1 if your nextflow version is between 20.10 and 22.10 \
Tip 3: Next to choosing the right sample_{NUMBER}.csv file you have to choose also the correct output directory!

However, there are are a great number of other possibilities, how to use nf-core/taxoprofiler. \
The script ```calculate_diversities.sh``` contains several parts and relies on python files in the directory modules.
Firstly, it creates a counting table per group out of the bracken outputs. Then it creates a file with different alpha diversity indices (shannon and simpson index).
The shannon indeces are used to create groupwise boxplots and compare them with a pairwise t-test. The alpha diversity index as well as the pairswise test can be changed manually in the script ```modules/alpha_ttest.py```. 
After that, it calculates the beta diversity of the sample between groups. But not the beta diversity of samples in the same group. From the different,calculated beta diversity indeces, the weighted jaccard dissimilarity is usded to create boxplots and is compared by a pairwise t-test. Again, this can be changed manually in the script ```modules/beta_ttest.py``` .
In order to run the whole diversity script, type:

```
bash calculate_diversities.sh
```


