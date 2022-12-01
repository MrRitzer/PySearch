from node import Node

class Ranked: 
    def __init__(self) -> None:
        self.__ranked = []

    def getRanked(self) -> list:
        temp = []
        for n in self.__ranked:
            temp.append(n.getUrl())
        return temp

    def getScored(self) -> list:
        temp = []
        for n in self.__ranked:
            temp.append({n.getUrl():n.getScore()})
        return temp

    def addNode(self, node: Node) -> None:
        for i,n in enumerate(self.__ranked):
            if node.getScore() > n.getScore():
                self.__ranked.insert(i,node)
                return
        self.__ranked.append(node)