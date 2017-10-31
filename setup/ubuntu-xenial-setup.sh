#!/bin/bash

# Update repository data
sudo apt-get update

sudo apt-get install aptitude -y

# Setup pre-reqs for Ansible install on Ubuntu
sudo apt-get install software-properties-common -y
sudo apt-add-repository ppa:ansible/ansible -y

# Update repo data now that be have the ansible PPA added
sudo apt-get update

# Install Ansible
# -- Also installs python2.7
sudo apt-get install ansible -y

# Install Python pip (for installing Python modules)
# --We install manually because the Ubuntu python-pip package is seriously out of date
wget https://bootstrap.pypa.io/get-pip.py
sudo /usr/bin/python2.7 get-pip.py
rm get-pip.py
