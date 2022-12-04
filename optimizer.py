from threading import Thread, Event, Semaphore
from urllib.parse import urlparse
from node import Node
from ranked import Ranked
from data import Data
import time

class Optimizer:
    def __init__(self) -> None:
        self.ranked = Ranked()
        self.__event = Event()
        self.__thread = Thread(target=self.__loop,args=())
        self.__thread.daemon = True
        self.__thread.start()

    def __loop(self) -> None:
        while True:
            self.__event.wait()
            for n in self.ranked.ranked:
                # if self.ranked.getSize() < Data.size:
                if len(Data.crawled) < Data.size:
                    if not Data.crawled.__contains__(n.getUrl()):
                        n.crawl()
                        Data.crawled.append(n.getUrl())
                        self.scoreLinks()
                else:
                    break
            self.__event.clear()

    def start(self) -> None:
        self.__event.set()

    def newNode(self,url) -> None:
        node = Node(url,2)
        Data.scored.append(url)
        Data.links.append(url)
        self.ranked.addNode(node)
        self.start()

    def scoreLinks(self):
        time.sleep(0.5)
        Data.sem.acquire()
        new = list((set(Data.scored) | set(Data.links)) - (set(Data.scored) & set(Data.links)))
        for url in new:
            score = self.calculateScore(url)
            node = Node(url,score)
            self.ranked.addNode(node)
            Data.scored.append(url)
        Data.sem.release()

    def calculateScore(self,url="") -> int:
        if len(Data.keywords) and Data.url == None:
            return 0
        score = 0
        try:
            if urlparse(url).netloc == urlparse(Data.url).netloc:
                score += 2
        except:
            pass
        try:
            for word in Data.keywords:
                if str(word).lower() in url.lower():
                    score += 1
        except:
            pass
        return score