#!/bin/bash
set -e

sleep 2
git pull
python3 deployer.py &