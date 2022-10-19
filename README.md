# IntensiviHomework
## Workflow status
![example workflow](https://github.com/liltousin/IntensiviHomework/actions/workflows/python-package.yml/badge.svg?event=push&name=flake8)
## Installation
### Windows
```bash
gh repo clone liltousin/IntensiviHomework
cd IntensiviHomework
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```
### Linux 
```bash
sudo apt install gh
gh repo clone liltousin/IntensiviHomework
cd IntensiviHomework
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
## Run
### Windows
```bash
python IntensiviHomework/manage.py runserver
```
### Linux
```bash
python3 IntensiviHomework/manage.py runserver
```
Then go to http://127.0.0.1:8000/
