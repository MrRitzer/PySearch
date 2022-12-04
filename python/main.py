# main.py
from urllib.parse import urlparse
from flask import Flask, request, Response, render_template
from threading import Thread
from search import SearchEngine

app = Flask(__name__)
se = SearchEngine()

@app.route("/api/startcrawl",methods = ['post'])
def startCrawl():
    se.clearSearch()
    try:
        keywords = request.json['keywords']
        se.setKeywords(keywords)
    except:
        pass
    try:
        url = request.json['url']
        if se.isValid(url):
            se.newSearch(url)
            return Response("Valid url", status=200, mimetype='application/json')
        else:
            return Response("Invalid/Missing url", status=400, mimetype='application/json')
    except:
        return Response("Invalid/Missing url", status=400, mimetype='application/json')

@app.route("/api/crawl")
def crawl():
    if se.canContinue():
        se.increaseSize(10)
        se.continueSearch()
        return Response("Valid url", status=200, mimetype='application/json')
    return Response("Missing url", status=400, mimetype='application/json')

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
    return {"size": se.getSize()}

@app.route("/api/getcrawled")
def getCrawled():
    return se.getCrawled()

@app.route("/api/getkeywords")
def getKeywords():
    return se.getKeywords()

# Only use this for debugging
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000,debug=True)