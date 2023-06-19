# Airbiome_Project
## Introduction
This reposatory contains the bioinformatics tools to analyse the Airbiome in Medellín.
The used workflows are using either [nextflow](https://www.nextflow.io/) with containers (Singularity, Docker,..) to ensure reproducibility.
It also contains bash and pyton scripts which do not need more than a few preinstalled packages to run.
## Requirements
-Nextflow version >= 20.10 but <=  22.10 \
-Java v11+ \
-Docker \
Information: All the pipelines are run using Docker to ensure portability. Python, R and other software/packages are installed inside the docker image.
## Documentation
This project uses [nf-co.re/taxprofiler](https://nf-co.re/taxprofiler/1.0.0) for reads preprocessing (otional), which incluedes adapter trimming and host removal, and taxonomic profiling with kraken2. nf-co.re/taxoprofiler has many other options, which can be activated. However, they are for this project not needed and therefore, not further mentioned in this github repo. For more detailed information, please click [here](https://nf-co.re/taxprofiler/1.0.0).  
This taxonomic pipeline uses Nextflow. It can use a variety of different containers such as Singularity, Docker, Podman, Shifter or Charliecloud. We recommend to install docker as it is used for all the other parts as well. As an input it accepts single or paired end fastq or even single end fasta files. Again, because the downstream analysis pipeline requires paired end reads, we recommend to used them instead of single end reads.\
To clone the repo and change to the main/ directory, type:

```
git clone https://github.com/engeleph/Airbiome_Project
cd main/
```

A kraken2 databese necessary could be downloaded [here](https://benlangmead.github.io/aws-indexes/k2).However, if the computational resources allow it, it is highly recommended to build the Kraken Database by running the python scripts in the directory build_kraken_db in order. However, 1.2 TB of memory is needed for the full size or 550 GB for a smaller version! After running the python scripts you have to run:

```
#command to build full size database
kraken2-build --build --db Kraken2_GTDB/  

#or for smaller database size
kraken2-build --build --db Kraken2_GTDB/ --max-db-size 500000000000
```

Before you can start using taxoprofiler change sample_{NUMBER}.csv and database.csv. Every group (month/PM size/ ...) needs an own sample_{NUMBER}.csv table! In order to do a taxonomic profiling with kraken2, run the following command:

```
NXF_VER=22.10.1 nextflow run nf-core/taxprofiler --input conf/sample_{NUMBER}.csv --databases conf/database.csv --outdir output_test/group_{NUMBER} -profile docker --run_kraken2 --run_bracken --max_memory '24 GB' --max_cpus 6
```
Tip 1: You can also create Krona plots (```--run_krona```) or do a taxonomic classification with metaphlan3 (```--run_metaphlan3```). \sklearn
Tip 2: You do not have to type NXF_VER=22.10.1 if your nextflow version is between 20.10 and 22.10 \
Tip 3: Next to choosing the right sample_{NUMBER}.csv file you have to choose also the correct output directory!

However, there are a great number of other possibilities, how to use nf-core/taxoprofiler. \
At this part you should build a docker image for the followings parts. Move one folder back to the Dockerfile and build.
For this run:

```
cd ..
docker build -t metagenomics_analysis .
```
After the docker image is built, open it with:

```
sudo docker run -v ./main:/main -ti -w="/main" --rm metagenomics_analysis /bin/bash
```

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

For the downstream analysis you have to move to the directrory Metagenomics_analysis/.

```

cd Metagenomics_analysis/

```
There, run first the script ```prepare_databases.sh```. It creates all the necessary databases for this part, such as humann2, megan, kraken, etc. Be aware that these databases need a lot of memory (~200 GB)!

```
bash prepare_databases.sh
```
After the script has finished you can run the main script ```metagenomics_analysis.sh```. This main script calls ceveral other script in this directory (run_*.sh). This multy step script starts with quality control of the reads and then continues with assembly, functional classification, comparative analysis and many more. In order to get mor detailed information about this downstream anylsis or in case of uncertainties click [here](https://github.com/grimmlab/MicrobiomeBestPracticeReview).

```
bash metagenomics_analysis.sh
```

When the pipeline has finished, close the docker image with Ctrl+d. All the results will be mounted to the local directory!
Now you can analyse the results ;)
