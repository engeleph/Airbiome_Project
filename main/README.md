# Airbiome_Project
## Introduction
This reposatory contains the bioinformatics tools to analyse the Airbiome in Medellín.
The used workflows are using either [nextflow](https://www.nextflow.io/) with containers (Singularity, Docker,..) to ensure reproducibility.
It also contains bash and pyton scripts which do not need more than a few preinstalled packages to run.
## Requirements
-Python v3 \
-Nextflow version >= 20.10 but <=  22.10 \
-Java v11+ \
-Singularity, Docker, Podman, Shifter or Charliecloud
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

Important: If the computational resources allow it, it is highly recommended to build the Kraken Database by running the python scripts in the directory build_kraken_db in order. However, 1.2 TB of memory is needed!

Before you can start using taxoprofiler change sample_{NUMBER}.csv and database.csv. Every group (month/PM size/ ...) needs an own sample_{NUMBER}.csv table! In order to do a txonomic profiling with kraken2 and metaphlan3 and produce krona plots, run the following command:

```
NXF_VER=22.10.1 nextflow run nf-core/taxprofiler --input conf/sample_{NUMBER}.csv --databases conf/database.csv --outdir output_test/group_{NUMBER} -profile docker --run_kraken2 --run_bracken --max_memory '24 GB' --max_cpus 6
```
Tip 1: You can also create Krona plots (```--run_krona```) or do a taxonomic classification with metaphlan3 (```--run_metaphlan3```). \sklearn
Tip 2: You do not have to type NXF_VER=22.10.1 if your nextflow version is between 20.10 and 22.10 \
Tip 3: Next to choosing the right sample_{NUMBER}.csv file you have to choose also the correct output directory!

However, there are a great number of other possibilities, how to use nf-core/taxoprofiler. \
The script ```calculate_diversities.sh``` contains several parts and relies on python files in the directory modules. Explanations of possible configurations are further discribed in the configfile ```conf/config.py```.
Firstly, it creates a counting table per group out of the bracken outputs. Next very low abundant OTUs can be filtered. For this a filter size and filter proportion can be chosen. The filter process can be easily described as all OTUs in one group are set to 0 when the average count is smaller or equal than the filter size and the the proportion of 0's is bigger than the filter proportion. The observed counts for these OTUs are viewed as false positive. To adjust for the potentially enormous differences between very highly abundant and very rare OTUs the OTU table is transformed. For that, the logarithmic transformation (log2(x+1)) is used. Configuration for these two steps can be specified in the config file. After finalizing the OTU table, it creates a file with different alpha diversity indices (shannon and simpson index). The desired alpha diversity index is used to create groupwise boxplots and compares this index between groups with the chosen test. After that, it calculates the beta diversity of the sample between groups. But not the beta diversity of samples in the same group. From the calculated beta diversity indeces, similar as for the alpha diversity, an index and a test can be specified in the config file.
In order to run the whole diversity pipeline, type:

```
bash calculate_diversities.sh
```

The script ```create_relative_abundance.sh``` uses the bracken output to create a table with the relative abundances of species for each group. This table is then used to creat a plot with the overall (over all groups) most common species. For this purpose, the overall mean of the diffennt species is calculated and then ordered. Only the x most abundant species are plotted. X can be chosen again in the config file.
Run this script by typing:

```
bash create_relative_abundance.sh
```

What also might be interesting is to search for common pathogens in the different groups. The script ```search_pathogens.py``` does exactly that. The output states if a pathogen is found (TRUE) or not (FALSE). Run it with:

```
python3 search_pathogens.py
```

The script ```calculate_CA.sh``` is helping to analyze the taxonimic data a bit more. Firstly, it creates a counting table over all samples of all groups. This counting table is the used to first calculate and plot the first two PC and color the data points by group. Then, it also calculates a CCA and uses a second table with the independent variables. The name of this tables has to be adjusted in the script ```modules/CCA.py```.
In order to run the whole pipeline, type:

```
bash calculate_CA.sh
```

