import requests
import re

#TODO: starting url as command line arg
#https://dev.to/fprime/how-to-create-a-web-crawler-from-scratch-in-python-2p46

class Crawler:
    def __init__(self, url):
        self.starting_url = url
        self.visited = set()

    def start(self):
        pass

if __name__ == "__main__":
    spider = Crawler("www.reddit.com")
    spider.start()

    