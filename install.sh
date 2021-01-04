#!/bin/bash

# Exit if any command fails
set -e

# Install Python3
sudo apt install python3

# Install pip
sudo apt install python3-pip

# Install pipenv
pip3 install pipenv

# Install python packages
pipenv install

# Install sqlite3 package
sudo apt install sqlite3
