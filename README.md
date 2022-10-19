# IntensiviHomework
## Workflow status
![flake8](https://github.com/liltousin/IntensiviHomework/actions/workflows/python-package.yml/badge.svg?event=push)
## Installation
### Windows
```bash
git clone https://github.com/liltousin/IntensiviHomework.git
cd IntensiviHomework
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
git update-index --assume-unchanged .env
```
### Linux 
```bash
git clone https://github.com/liltousin/IntensiviHomework.git
cd IntensiviHomework
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
git update-index --assume-unchanged .env
```
## Setting up env
### Description
The .evn file already has a test configuration. Any local parameter changes will not be tracked by the git. Just plug and play.
### How to write the parameters
Any string is passed to the SECRET_KEY parameter
The parameter DEBUG can have only 2 values ('True' or 'False')
Into ALLOWED_HOSTS parameter you have to write the hosts, separated by comma with space (", ")
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
