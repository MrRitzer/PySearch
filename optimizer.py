from threading import Thread, Event
from urllib.parse import urlparse
from node import Node
from ranked import Ranked

class Optimizer:
    def __init__(self) -> None:
        self.links = dict()
        self.ranked = Ranked()
        self.url = None
        self.keywords = []
        self.scored = []
        self.thread = Thread(target=self.__loop__, args=())
        self.thread.daemon = True
        self.event = Event()
        self.thread.start()

    def __loop__(self) -> None:
        while True:
            self.event.wait()
            keys = list(self.links.keys())
            for i in range(0,len(keys)):
                url = keys[i]
                if self.scored.__contains__(url):
                    continue
                else:
                    score = self.scoreNode(url)
                    node = Node(url,score)
                    self.ranked.addNode(node)
                    self.scored.append(url)
            self.event.clear()

    def run(self) -> None:
        self.event.set()

    def scoreNode(self,url="") -> int:
        if len(self.keywords) and self.url == None:
            return 0
        score = 0
        try:
            if urlparse(url).netloc == urlparse(self.url).netloc:
                score += 2
        except:
            pass
        try:
            for word in self.keywords:
                if word in url:
                    score += 1
        except:
            pass
        return score

    def setUrl(self,url) -> None:
        self.url = url

    def setKeywords(self,keywords) -> None:
        self.keywords = keywords

    def getRanked(self) -> list:
        return self.ranked.getRanked()

    def getScored(self) -> list:
        return self.ranked.getScored()