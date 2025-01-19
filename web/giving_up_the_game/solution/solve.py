import requests
import base64

url = "http://34.135.223.176:7845/getSprites"
r = requests.get(url)
print(base64.b64decode(r.text))