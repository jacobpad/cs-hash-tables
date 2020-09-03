"""
In a loop:
    Enter a URL: [you enter a URL]
    [shows the data from that URL]

It also caches that data so subsequent requests for the same URL simply
return the cached data. Intead of going over the network again.

Stuff to figure out:
x How to get data from a URL
x How are we going to cache it?
* What happens if the server gets updated?

"""

import urllib.request
import datetime

class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()


MAX_AGE = 10  # seconds

cache = {}

while True:
    url = input("Enter a URL: ")

    cur_time = datetime.datetime.now().timestamp()

    if url not in cache or cur_time - cache[url].timestamp > MAX_AGE:
        print("CACHE MISS")

        with urllib.request.urlopen(url) as response:
            data = response.read()

        cache[url] = CacheEntry(data)

    else:
        print("CACHE HIT")

    print(cache[url].data[:65])


