#!/bin/bash

#this script installs all necessary python packages for this project

#numpy and pandas are essential for databases in python
pip3 install numpy
pip3 install pandas

#argaprse is important to give a python file input variables
pip3 install argparse

#scipy is used to calculate test statistics
pip3 install scipy

#matplotlib.pyplot helps us to create nice plots
pip3 install matplotlib.pyplot 

#seaborn willl be used to create a nice boxplot including pairwise tests
pip3 install seaborn

#statannot is needed by seaborn to plot significance of the tests
pip3 install statannot
