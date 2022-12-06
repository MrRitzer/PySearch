# PySearch: A Python web crawler with an Angular frontend

## About

PySearch is a simple web crawler that was built using the Python [Flask](https://flask.palletsprojects.com/en/2.2.x/) for the backend API and [Angular](https://angular.io/) for the frontend. The client recieves updates by periodically polling the server, asking if there is new data. The server determines the most relevant search results by checking the found urls for keywords to determine if the search is relevant or not, this is not the most optimized way to determine importance but due to lack of computing resources it was the most effecient we found for quickly determing relavance of a found url, however, the application was designed in such a way that this could be easily updated to also check page contents for found urls.

## Requirements
* [NodeJS](https://nodejs.org/en/)
* [AngularCLI](https://angular.io/cli)
* [Python](https://www.python.org/) <i>>3.10.6</i>
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)

## Running the packages
### Flask API (Do this in python folder)
1. Create virtual environment

    A. Windows: `python3 -m venv env`

    B. MacOS: `python3 -m venv ./env`
2. Activate virtual environment

    A. Windows: `env\Scripts\activate`

    B. MacOS: `source ./env/bin/activate`

3. Install requirements: `pip install -r requirements.txt`

4. Run `python main.py`

### Angular Client (Do this in searchapp folder)
1. Install packages: `npm install`

2. Run client: `ng serve`