from node import Node

class Ranked: 
    def __init__(self) -> None:
        self.ranked = []

    def addNode(self, node: Node) -> None:
        for i,n in enumerate(self.ranked):
            if node.getScore() > n.getScore():
                self.ranked.insert(i,node)
                return
        self.ranked.append(node)

    def getMax(self) -> int:
        return self.ranked[0].getScore()

    def getSize(self) -> int:
        return len(self.ranked)

    def getRanked(self) -> list:
        temp = []
        for n in self.ranked:
            temp.append(n.getUrl())
        return temp

    def getScored(self) -> list:
        temp = []
        for n in self.ranked:
            temp.append({n.getUrl():n.getScore()})
        return temp

    def getTitle(self) -> list:
        temp = []
        for n in self.ranked:
            temp.append({"Title":n.getTitle()})
        return temp

    def getLinks(self) -> list:
        temp = []
        for n in self.ranked:
            temp.append({"url":n.getUrl()})
        return temp

    def getFormal(self) -> list:
        temp = []
        for n in self.ranked:
            temp.append({n.getTitle():n.getUrl()})
        return temp