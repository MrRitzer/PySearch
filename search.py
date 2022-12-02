from optimizer import Optimizer
from validators import url as urlValidator
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from data import Data

class SearchEngine:
    def __init__(self) -> None:
        self.opt = Optimizer()

    def clearSearch(self) -> None:
        Data.keywords = []
        Data.crawled = []
        Data.scored = []
        Data.url = None

    def newSearch(self,url) -> None:
        Data.url = url
        self.opt.newNode(url)

    def continueSearch(self) -> None:
        self.opt.crawl()

    def increaseSize(self,size) -> None:
        Data.size += size

    def setKeywords(self,keywords) -> None:
        temp = []
        for keyword in keywords:
            temp.append(keyword['key'])
        Data.keywords = temp

    def canContinue(self) -> bool:
        return Data.url != None

    def isValid(self,url) -> bool:
        return urlValidator(url)

    def getLinks(self) -> list:
        return self.opt.ranked.getLinks()

    def getRanked(self) -> list:
        return self.opt.ranked.getRanked()

    def getScored(self) -> list:
        return self.opt.ranked.getScored()

    def getFormal(self) -> list:
        return self.opt.ranked.getFormal()

    def getCrawled(self) -> list:
        return Data.crawled

    def getKeywords(self) -> list:
        return Data.keywords