from threading import Thread, Event, Semaphore
from urllib.parse import urlparse
from node import Node
from ranked import Ranked
from data import Data

class Optimizer:
    def __init__(self) -> None:
        self.ranked = Ranked()
        self.__thread = Thread(target=self.run,args=())
        self.__thread.daemon = True
        self.__thread.start()
        self.sem = Semaphore(0)

    def run(self) -> None:
        while True:
            self.sem.acquire()
            for n in self.ranked.ranked:
                if self.ranked.getSize() < Data.size:
                    if Data.scored.__contains__(n):
                        continue
                    else:
                        self.scoreNode(n)
                else:
                    break
            self.sem.release()

    def start(self) -> None:
        self.__sem.release()

    def newNode(self,url) -> None:
        node = Node(url)
        node.setScore(2)
        node.crawl()
        self.ranked.addNode(node)

    def scoreNode(self,node:Node):
        node.sem.acquire()
        print("Aquired!")
        nodes = node.getLinks()
        for n1 in nodes:
            for n2 in Data.scored:
                if n1.getUrl() == n2.getUrl():
                    n1.setScore(n2.getScore())
                    break
            score = self.calculateScore(n1.getUrl())
            n1.setScore(score)
            self.ranked.addNode(n1)
            Data.scored.append(n1)
        node.sem.release()

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