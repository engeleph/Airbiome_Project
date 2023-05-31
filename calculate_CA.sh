#!/bin/bash

#create counting table over all groups
python3 modules/create_overall_table.py

#create PCA plot with 2 PCs
python3 modules/PCA.p#!/bin/bash

#create counting table over all groups
python3 modules/create_overall_table.py

#create PCA plot with 2 PCs
python3 modules/PCA.py

#calculates the first two correlation dimensions of CA and plot them
python3 modules/CCA.py
