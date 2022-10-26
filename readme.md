# PySearch
## Description
A simple search engine web crawler implemented using Python. The application can be manually built and installed or ran using docker.

## Prereqisites
* [Python](https://www.python.org/downloads/)
* [Virtualenv](https://pypi.org/project/virtualenv/)

## Installation
1. Create virtual environment
    
    A. Windows: `python3 -m venv env`

    B. MacOS: `python3 -m venv ./env`


2. Activate virtual environment

    A. Windows: `env\Scripts\activate`

    B. MacOS: `source ./env/bin/activate`
3. Install requirements: `pip install -r requirements.txt`

_Note_: To decativate virtual environment: `deactivate`

## Docker Installation
1. Build docker image: `docker build -t pysearch .`
2. Run docker image: `docker run pysearch`
