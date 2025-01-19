import hashlib
import base64

target = "aac56acc457c9cf0f15ad8d20347b7aa"
with open("/usr/share/wordlists/rockyou_utf8.txt", "r") as f:
    z = lambda x : x.strip()
    lines = map(z, f.readlines())

for l in lines:
    encoded = base64.b64encode(l.encode())[::-1]
    result = hashlib.md5(encoded)
    if result.digest().hex() == target:
        print(l)
        exit(0)

# yougotserved
