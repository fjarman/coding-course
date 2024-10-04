#!/bin/bash
set -e

adduser deployer
su deployer
cd ~/
ssh-keygen -t rsa -b 4096
