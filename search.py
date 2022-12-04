from optimizer import Optimizer
from validators import url as urlValidator
from data import Data

class SearchEngine:
    def __init__(self) -> None:
        self.opt = Optimizer()

    def clearSearch(self) -> None:
        self.opt = Optimizer()
        Data.reset()

    def newSearch(self,url) -> None:
        Data.url = url
        self.opt.newNode(url)

    def continueSearch(self) -> None:
        self.opt.start()

    def increaseSize(self,size) -> None:
        Data.size += size

    def getSize(self) -> int:
        return Data.size

    def setKeywords(self,keywords) -> None:
        Data.keywords = keywords

    def canContinue(self) -> bool:
        return Data.url != None

    def isValid(self,url) -> bool:
        return urlValidator(url)

    def getLinks(self) -> list:
        return Data.links

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