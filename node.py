class Node:
    def __init__(self,url,score=0) -> None:
        self.__score = score
        self.__url = url

    def setScore(self,score) -> None:
        self.__score = score

    def getScore(self) -> int:
        return self.__score

    def getUrl(self) -> str:
        return self.__url

    def __str__(self) -> str:
        return "Url: " + self.__url + ", Score: " + str(self.__score)

    def __repr__(self) -> str:
        return "Url: " + self.__url + ", Score: " + str(self.__score)