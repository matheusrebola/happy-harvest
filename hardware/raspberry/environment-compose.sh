#!/bin/bash

# Atualizar o sistema
sudo apt-get update
sudo apt-get upgrade -y

# Instalar Python e pip
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y

# Instalar requests
pip3 install requests
