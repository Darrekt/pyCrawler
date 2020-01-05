# pyCrawler
This repository contains a simple Python script that implements a depth/breadth-first web crawler (on separate branches).

The crawler uses some packages: 
* sys - for command line arguments
* request - to make http(s) GET requests to urls and fetch the html source.
* re - regex library used for regex matching of `<a href="...">` tags to parse URLs in a capturing group.
* urlparse - breaks down a URL into an object with the scheme (https), netloc (www.reddit.com) and page (/r/gaming).

## Requirements
* Latest version of Python3

## Usage
Run application: Simply run with python3, inputting a website as a command line argument with the HTTP(S) scheme in front.

```console
$ python3 crawler.py http://crawl-a-website.com
```

## Known issues / Potential Optimisations

1. Currently does not differentiate two urls as unique with trailing '/'s, '#'s, or http vs https. i.e. https://reddit.com/ and https://reddit.com. An attempt has been made to remove the trailing '/'s with the rstrip() function, but is not working yet. Another possible fix would be to optimise the regex to omit trailing '/'s when a given string ends with one.

2. Some sites actively try to blacklist web crawlers by not accepting too many http requests from a single host within a short timeframe. This can be circumvented by using a rotating proxy API. Or, if one desires implementation from scratch, the requests package supports the use of proxies by accepting an argument that expects a dictionary of proxy IP addresses. More information can be found on the request docs [here](https://2.python-requests.org//en/latest/user/advanced/#proxies)
