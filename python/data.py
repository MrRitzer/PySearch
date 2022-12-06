from threading import Semaphore

class Data:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    url = None
    links = []
    keywords = []
    crawled = []
    scored = []
    sem = Semaphore()
    hasUpdated = False
    size = 10

    def reset() -> None:
        Data.url = None
        Data.links = []
        Data.keywords = []
        Data.crawled = []
        Data.scored = []
        Data.sem = Semaphore()
        Data.hasUpdated = False
        Data.size = 10