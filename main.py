# main.py
from flask import Flask, redirect, request, url_for, Response
from threading import Thread
from search import SearchEngine

app = Flask(__name__)

se = SearchEngine()

@app.route("/api/startcrawl",methods = ['post'])
def crawl():
    try:
        url = request.json['url']
        if se.isValid(url):
            se.setUrl(url)
            se.increaseSize(100)
            Thread(target=se.crawl, args=()).start()
            return Response("Valid url", status=200, mimetype='application/json')
    except:
        if se.containsUrl():
            se.increaseSize(100)
            Thread(target=se.crawl, args=()).start()
            return Response("Valid url", status=200, mimetype='application/json')
        return Response("Invalid/Missing url", status=400, mimetype='application/json')

@app.route("/api/getlinks")
def getLinks():
    return se.getLinks()

@app.route("/api/getcrawled")
def getCrawled():
    return se.getCrawled()

@app.route('/')
def base():
    return redirect(url_for('index'), code=302)

@app.route("/index")
def index():
    return "Index Page"

# Only use this for debugging
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000,debug=True)