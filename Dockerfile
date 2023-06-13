#ARG CODE_BASE="/opt/Airbiome_Project"

FROM metabat/metabat:latest

COPY . .

FROM ubuntu:20.04

RUN export DEBIAN_FRONTEND="noninteractive" && apt-get update && apt-get install -y \
    autoconf \
    automake \
    binutils-dev \
    ccache \
    curl \
    g++-10 \
    git \
    make \
    pkg-config \
    python3 \
    python3-pip \
    python3-venv \
    vim \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

#RUN add-apt-repository -y ppa:mercurial-ppa/releases
RUN python3 -m pip install mercurial --default-timeout=900

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get -y install default-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#RUN perl -MCPAN -e 'install XML::Simple'

RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install argparse
RUN pip3 install scipy
RUN pip3 install matplotlib
RUN pip3 install seaborn
RUN pip3 install statannot
RUN pip3 install bokeh
RUN python3 -m pip install -U plotly
RUN pip3 install -U kaleido
RUN pip3 install scikit-learn

#COPY ./conf/ .
#COPY ./modules/ .
#COPY ./build_kraken_db/ .
#COPY ./output_analysis/ .
#COPY ./output_test/ .
#COPY ./search_patogens.py .
#COPY ./calculate_diversities.sh .
#COPY ./calculate_CA.sh .
#COPY ./create_relative_abundance.sh .

COPY . .
#WORKDIR ./Airbiome_Project

#FROM metabat/metabat:latest

#COPY . .
