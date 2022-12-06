from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from threading import Thread, Event, Semaphore
import requests
from data import Data

class Node:
    def __init__(self,url: str,score: int) -> None:
        self.__score = score
        self.__url = url
        self.__title = None
        self.__description = None
        self.__thread = Thread(target=self.__run, args=())
        self.__thread.daemon = True

    def setScore(self,score) -> None:
        self.__score = score

    def getScore(self) -> int:
        return self.__score

    def getUrl(self) -> str:
        return self.__url

    def getTitle(self) -> str:
        return self.__title

    def getDescription(self) -> str:
        return self.__description

    def crawl(self) -> None:
        self.__thread.start()

    def __run(self) -> None:
        url = self.__url
        baseUrl = urlparse(url).netloc
        f = requests.get(url,headers=Data.headers)
        soup = BeautifulSoup(f.content,'lxml')
        self.__title = soup.find('title').string
        tags = soup.find_all('a')
        Data.sem.acquire()
        for link in tags:
            try:
                newUrl = None
                temp = str(link['href'])
                if temp[0] != "#":
                    if temp[0:2] == "//":
                        newUrl = str("https:"+temp)
                    elif temp[0] == "/":
                        newUrl = str("https://" + baseUrl + temp)
                    elif temp.find("http") != -1 or temp.find("https") != -1 :
                        newUrl = str(temp)
                    if not Data.links.__contains__(newUrl):
                        Data.links.append(newUrl)
            except:
                continue
        Data.sem.release()