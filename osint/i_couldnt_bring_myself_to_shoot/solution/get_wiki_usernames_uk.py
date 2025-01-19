#!/usr/bin/python3
from typing import Iterator
import logging
from pathlib import Path

logging.basicConfig(format="'%(asctime)s - %(levelname)s - %(message)s", filename=f"{Path(__file__).stem}.log", level=logging.DEBUG)
log = logging.getLogger(__name__)


import requests
from collections import deque

s = requests.Session()
url = "https://en.wikipedia.org/w/api.php"


def query_nearby(lat: int | float, long: int | float) -> Iterator[str]:
    params = {
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{long}",
        "gslimit": "10",
        "gsradius": "10000", # in meters
        "action": "query"
    }

    r = s.get(url=url, params=params)
    data = r.json()
    places = data['query']['geosearch']

    for place in places:
        yield place['title']


def get_coords(title: str) -> (float, float):
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "coordinates"
    }

    r = s.get(url=url, params=params)
    data = r.json()
    pages = data['query']['pages']

    for k, v in pages.items():
        return v['coordinates'][0]['lat'], v['coordinates'][0]['lon']


def query_revisions(title: str):
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvprop": "user|userid",  #"timestamp|user|comment|userid",
        "rvslots": "main",
        "formatversion": "2",
        "format": "json",
        "rvlimit": 500,
    }

    r = s.get(url=url, params=params)
    data = r.json()

    pages = data["query"]["pages"]

    for page in pages:
        for rev in page['revisions']:
            username = rev["user"]
            print(username, flush=True)
            userid = rev['userid']
            print(userid, flush=True)


vis = set()
d = deque()
starting_article = "Filey"
vis.add(starting_article)
d.append(starting_article)

max_pages = 1000000
i = 0
with open("wiki_pages.txt", "w") as f_out:
    while d and i < max_pages:
        curr_title = d.popleft()
        try:
            query_revisions(curr_title)
            curr_lat, curr_long = get_coords(curr_title)
            for p in query_nearby(curr_lat, curr_long):
                if p in vis:
                    continue
                vis.add(p)
                d.append(p)
                print(p, file=f_out, flush=True)
                i += 1
        except Exception as e:
            log.error("Exception occurred", exc_info=e)
            continue