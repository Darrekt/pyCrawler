import requests
import re
from urllib.parse import urlparse

# TODO: starting url as command line arg
# https://dev.to/fprime/how-to-create-a-web-crawler-from-scratch-in-python-2p46


class Crawler:

    def __init__(self, url):
        self.starting_url = url
        self.visited = set()

    def fetch_html(self, url):
        try:
            html = requests.get(url)
        except Exception as e:
            print(e)
            return ""
        return html.content.decode('latin-1')

    def get_links(self,url):
        html = self.fetch_html(url)
        #parses link into scheme, netloc and path
        parsed = urlparse(url) 

        #fancy string formatting
        base = f"{parsed.scheme}://{parsed.netloc}"

        #regex catch, links is a list of the caught groups
        links = re.findall( r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"', html)
        
        for i, link in enumerate(links):
            if not urlparse(link).netloc:
                full_link = base + link
                links[i] = full_link

        #remove email links
        return set(filter(lambda x: 'mailto' not in x, links))

    def crawl(self,url):
        for link in self.get_links(url):
            if link in self.visited:
                continue
            print(link)
            #add the link to the list of visited urls
            self.visited.add(link)
            #currently depth-first
            self.crawl(link)

    def start(self):
        self.crawl(self.starting_url)

if __name__ == "__main__":
    spider = Crawler("http://www.reddit.com")
    spider.start()