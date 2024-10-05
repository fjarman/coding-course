#!/bin/bash
set -e

sleep 1
git pull
pip3 install -r requirements.txt

current_date=$(date -u)
echo "$current_date" > last_deployment.txt

python3 deployer.py &