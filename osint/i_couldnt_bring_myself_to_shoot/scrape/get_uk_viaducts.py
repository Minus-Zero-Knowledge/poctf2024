#!/usr/bin/python3

import requests
import logging
from pathlib import Path

logging.basicConfig(format="'%(asctime)s - %(levelname)s - %(message)s", filename=f"{Path(__file__).stem}.log", level=logging.DEBUG)
log = logging.getLogger(__name__)

s = requests.Session()
url = "https://en.wikipedia.org/w/api.php"


#https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links&titles=List of railway bridges and viaducts in the United Kingdom&pllimit=500
def get_links(title: str) -> list[str]:
    results = []
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "links",
        "pllimit": 500
    }

    while True:
        r = s.get(url=url, params=params)

        data = r.json()
        pages = data['query']['pages']

        for pid, page_links in pages.items():
            for l in page_links['links']:
                results.append(l['title'])

        if 'continue' in data:
            params['plcontinue'] = data['continue']['plcontinue']
        else:
            break

    return results


def query_revisions(title: str):
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvprop": "user|userid",
        "rvslots": "main",
        "formatversion": 2,
        "format": "json",
        "rvlimit": 500,
    }

    r = s.get(url=url, params=params)
    data = r.json()

    pages = data["query"]["pages"]

    for page in pages:
        for rev in page['revisions']:
            yield rev


def main():
    userids = set()
    usernames = set()

    for title in get_links("List of railway bridges and viaducts in the United Kingdom"):
        try:
            for rev in query_revisions(title):
                if (username := rev.get("user", None)) and username not in usernames:
                    print(username)
                    usernames.add(username)

                if (userid := rev.get("userid", None)) and userid not in userids:
                    print(userid)
                    userids.add(userid)

        except Exception as e:
            log.error("Exception occurred", exc_info=e)
            continue


if __name__ == '__main__':
    main()