#!/bin/bash
sudo apt-get -y update && apt-get -y upgrade
sudo apt-get install -y curl
sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev libpq-dev
sudo wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz 
sudo tar xzf Python-3.10.2.tgz 
cd Python-3.10.2 && ./configure --enable-optimizations && make altinstall
rm -r Python-3.10.2
rm Python-3.10.2.tgz
sudo python3.10 -m pip install --upgrade pip
pip3.10 install django
pip3.10 install pyTelegramBotAPI
pip3.10 install django_q
pip3.10 install python-dotenv
pip3.10 install redis
pip3.10 install bs4
pip3.10 install lxml
pip3.10 install django-ckeditor
pip3.10 install psutil
pip3.10 install pillow