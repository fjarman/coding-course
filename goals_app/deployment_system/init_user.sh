#!/bin/bash
set -e


apt-get install git python3-pip
adduser deployer
su deployer
cd ~/
ssh-keygen -t rsa -b 4096
