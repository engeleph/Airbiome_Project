# Airbiome_Project
This reposatory contains the bioinformatics tools to analyse the Airbiome in Medellín.
The used workflows are using either nextflow[1] with containers (Singularity, Docker,..) to ensure reproducibility.
It also contains bash and pyton scripts which do not need more than a few preinstalled packages to run.
## requisatory softwares for whole project
-Python3  \
-Nextflow version >= 20.10 but <=  22.10 \
-Java v11+ \
-Singularity, Docker, Podman, Shifter or Charliecloud 
## Reads preprocessing and taxonomic profiling 
This project uses nf-co.re/taxprofiler[2] for the reads preprocessing, taxonomic profiling and krona plots.  
This taxonomic pipeline  uses Nextflow. It can use a variety of different 
containers such as Singularity, Docker, Podman, Shifter or Charliecloud. As an input it accepts single or 
paired end fastq or even single end fasta files. The pipeline starts with adapter trimming and filtering. 
It does then a taxonomic classification with kraken2 and/or MetaPhlAn3. It uses then the output to create krona plots. 
For every step it can be chosen wheter it is made. For more detailed information, please click here. 
