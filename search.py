import requests
import lxml
import httpx
import asyncio
from validators import url as urlValidator
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# url = "https://www.rottentomatoes.com/top/bestofrt/"
6 
class SearchEngine:
    def __init__(self) -> None:
        self.links = []
        self.size = 1000
        self.keywords = []
        self.crawled = []
        self.loc = 0
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
        
    def setUrl(self,url) -> None:
        self.links.append(url)

    def containsUrl(self) -> bool:
        if len(self.links) > 0:
            return True
        return False

    def increaseSize(self,val) -> None:
        self.size += val

    def isValid(self,url) -> bool:
        return urlValidator(url)

    def getLinks(self) -> list:
        return self.links

    async def crawl(self) -> None:
        async with httpx.AsyncClient(headers=self.headers) as session:
            while True:
                url = self.links[self.loc]
                if self.crawled.__contains__(url):
                    print("Next url")
                    self.loc += 1
                else:
                    break
            baseUrl = urlparse(url).netloc
            f = await session.get(url)
            # f = requests.get(url,headers=self.headers)
            soup = BeautifulSoup(f.content,'lxml')
            tags = soup.find_all('a')
            local = []
            remote = []
            for link in tags:
                try:
                    temp = str(link['href'])
                    if temp[0] != "#":
                        if temp[0:2] == "//":
                            remote.append("https:"+temp)
                        elif temp[0] == "/":
                            local.append("https://" + baseUrl + temp)
                        elif temp.find("http") != -1 or temp.find("https") != -1 :
                            remote.append(temp)
                except:
                    continue
            self.crawled.append(url)
            self.links += list(set(local+remote))
            if len(self.links) < self.size:
                await self.crawl()