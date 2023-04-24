# Airbiome_Project
This reposatory contains the bioinformatics tools to analyse the Airbiome in Medellín.
The used workflows are using either nextflow[1] with containers (Singularity, Docker,..) to ensure reproducibility.
It also contains bash and pyton scripts which do not need more than a few preinstalled packages to run.
## requisatory softwares for whole project
-Python3 with packages numpy and pandas \
-Nextflow version >= 20.10 but <=  22.10 \
-Java v11+ \
-Singularity, Docker, Podman, Shifter or Charliecloud 
## Reads preprocessing and taxonomic profiling 
This project uses nf-co.re/taxprofiler[2] for the reads preprocessing, taxonomic profiling and krona plots.  
This taxonomic pipeline  uses Nextflow. It can use a variety of different 
containers such as Singularity, Docker, Podman, Shifter or Charliecloud. As an input it accepts single or 
paired end fastq or even single end fasta files. The pipeline starts with adapter trimming and filtering. 
It does then a taxonomic classification with kraken2 and/or MetaPhlAn3. It uses then the output to create krona plots. 
For every step it can be chosen wheter it is made. For more detailed information, please click [here](https://nf-co.re/taxprofiler/1.0.0). \
Databeses necessary for kraken2 or metaphlan3 should be downloaded [here](https://benlangmead.github.io/aws-indexes/k2) or with the following command, respectively: 

```
wget https://zenodo.org/record/4629921/files/metaphlan_databases.tar.gz \
tar -xzf metaphlan_databases.tar.gz
```

In order to do a txonomic profiling with kraken2 and metaphlan3 and produce krona plots

