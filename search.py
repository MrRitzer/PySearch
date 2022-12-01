import requests
from optimizer import Optimizer
from node import Node
from validators import url as urlValidator
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class SearchEngine:
    def __init__(self) -> None:
        self.opt = Optimizer()
        self.size = 100
        self.url = ""
        self.keywords = []
        self.crawled = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
        
    def setUrl(self,url) -> None:
        self.url = url
        self.opt.setUrl(url)
        self.opt.links.update({str(url):10})

    def setKeywords(self,keywords) -> None:
        for keyword in keywords:
            self.keywords.append(keyword['key'])
        self.opt.keywords = self.keywords

    def containsUrl(self) -> bool:
        if len(self.opt.links) > 0:
            return True
        return False

    def increaseSize(self,val) -> None:
        self.size += val

    def isValid(self,url) -> bool:
        return urlValidator(url)

    def getLinks(self) -> list:
        return list(self.opt.links)

    def getCrawled(self) -> list:
        return self.crawled
    
    def getRanked(self) -> list:
        return self.opt.getRanked()

    def getScored(self) -> list:
        return self.opt.getScored()

    def getKeywords(self) -> list:
        return self.keywords

    def crawl(self) -> None:
        if len(list(self.opt.links.keys())) == 1:
            url = list(self.opt.links.keys())[0]
        else:
            urls = list(self.opt.links.keys())
            loc = 0
            while True:
                url = urls[loc]
                if self.crawled.__contains__(url):
                    loc += 1
                else:
                    break
        baseUrl = urlparse(url).netloc
        f = requests.get(url,headers=self.headers)
        soup = BeautifulSoup(f.content,'lxml')
        tags = soup.find_all('a')
        for link in tags:
            try:
                newUrl = self.url
                temp = str(link['href'])
                if temp[0] != "#":
                    if temp[0:2] == "//":
                        newUrl = str("https:"+temp)
                    elif temp[0] == "/":
                        newUrl = str("https://" + baseUrl + temp)
                    elif temp.find("http") != -1 or temp.find("https") != -1 :
                        newUrl = str(temp)
                    self.opt.links.update({newUrl:0})
            except:
                continue
        self.crawled.append(url)
        self.opt.run()
        if len(self.opt.links) < self.size:
            self.crawl()