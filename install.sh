#!/usr/bin/bash

sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0

python3 -m venv --without-pip venv &&\
source ./venv/bin/activate &&\
python --version &&\
wget https://bootstrap.pypa.io/get-pip.py &&\
python get-pip.py &&\
pip --version &&\
pip install pycairo &&\
pip install PyGObject &&\
rm get-pip.py &&\
echo OK || {
  1>&2 echo Fail
  exit 1
}