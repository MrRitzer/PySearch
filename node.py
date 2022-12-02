from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from threading import Thread, Event, Semaphore
import requests
from data import Data

class Node:
    def __init__(self,url) -> None:
        self.__score = 0
        self.__url = url
        self.__title = None
        self.__description = None
        self.__links = set({})
        self.__thread = Thread(target=self.__run, args=())
        self.__thread.daemon = True
        self.__event = Event()
        self.sem = Semaphore()
        self.__thread.start()

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

    def getLinks(self) -> set:
        return self.__links

    def crawl(self) -> None:
        self.__event.set()

    def __run(self) -> None:
        while True:
            self.__event.wait()
            self.sem.acquire()
            if len(self.__links) == 0:
                url = self.__url
                baseUrl = urlparse(url).netloc
                f = requests.get(url,headers=Data.headers)
                soup = BeautifulSoup(f.content,'lxml')
                tags = soup.find_all('a')
            else:
                url = self.__url
                urls = self.__links
                loc = 0
                while True:
                    url = urls[loc].getUrl()
                    if Data.crawled.__contains__(url):
                        loc += 1
                    else:
                        break
            for link in tags:
                try:
                    newUrl = self.__url
                    temp = str(link['href'])
                    if temp[0] != "#":
                        if temp[0:2] == "//":
                            newUrl = str("https:"+temp)
                        elif temp[0] == "/":
                            newUrl = str("https://" + baseUrl + temp)
                        elif temp.find("http") != -1 or temp.find("https") != -1 :
                            newUrl = str(temp)
                        self.__links.add(Node(newUrl))
                except:
                    continue
            Data.crawled.append(url)
            self.sem.release()
            self.__event.clear()
