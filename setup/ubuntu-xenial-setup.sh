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
