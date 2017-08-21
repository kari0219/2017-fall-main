#!/bin/bash

set -x

# Don't download stuff to the git repo, that's messy.
pushd ${HOME}

# Update packages
sudo apt-get update
sudo apt-get upgrade

ANACONDA_INSTALLER="Anaconda2-4.3.1-Linux-x86_64.sh"
wget "https://repo.continuum.io/archive/$ANACONDA_INSTALLER"
bash "$ANACONDA_INSTALLER"

source ${HOME}/.bashrc

TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.1.0-cp27-none-linux_x86_64.whl
${HOME}/anaconda2/bin/pip install --upgrade pip
${HOME}/anaconda2/bin/pip install $TF_BINARY_URL
${HOME}/anaconda2/bin/jupyter notebook --generate-config

# Copy Jupyter config
popd
cp -v $(dirname $0)/support/jupyter_notebook_config.py ${HOME}/.jupyter/jupyter_notebook_config.py
