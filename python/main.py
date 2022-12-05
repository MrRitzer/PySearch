# main.py
from urllib.parse import urlparse
from flask import Flask, request, Response, render_template, make_response
from flask_cors import CORS
from threading import Thread
from search import SearchEngine
from data import Data

app = Flask(__name__)
CORS(app)
se = SearchEngine()

@app.route("/api/startcrawl",methods = ['POST'])
def startCrawl():
    se.clearSearch()
    try:
        keywords = request.get_json()['keywords']
        se.setKeywords(keywords)
    except:
        pass
    try:
        url = request.get_json()['url']
        if se.isValid(url):
            se.newSearch(url)
            # return Response("Valid url", status=200, mimetype='application/json')
            return {"data": "Valid url"}, 200
        else:
            # return Response("Invalid/Missing url", status=400, mimetype='application/json')
            return {"data": "Invalid/Missing url"}, 200
    except:
        # return Response("Invalid/Missing url", status=400, mimetype='application/json')
        return {"data": "Invalid/Missing url"}, 200

@app.route("/api/crawl")
def crawl():
    if se.canContinue():
        se.increaseSize(10)
        se.continueSearch()
        # return Response("Valid url", status=200, mimetype='application/json')
        return {"data": "Valid url"}, 200
    # return Response("Missing url", status=400, mimetype='application/json')
    return {"data": "Invalid/Missing url"}, 400



@app.route("/api/getlinks")
def getLinks():
    return se.getLinks()

@app.route("/api/getranked")
def getRanked():
    return se.getRanked()

@app.route("/api/getscored")
def getScored():
    return se.getScored()

@app.route("/api/getformal")
def getFormal():
    return se.getFormal()

@app.route("/api/getsize")
def getSize():
    return {"data": se.getSize()}

@app.route("/api/getcrawled")
def getCrawled():
    return se.getCrawled()

@app.route("/api/getkeywords")
def getKeywords():
    return se.getKeywords()

@app.route("/api/poll")
def poll():
    return se.poll()

@app.route("/api/test",methods = ['GET','POST'])
def test():
    try:
        print(request.get_json())
    except:
        pass
    return {'data': "Hello"}

# Only use this for debugging
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000,debug=True)