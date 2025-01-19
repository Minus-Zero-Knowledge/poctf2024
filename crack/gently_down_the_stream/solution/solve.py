from Crypto.Cipher import ARC4
import re
from tqdm import tqdm

ct_hex = "71 81 13 f7 f7 b2 87 bd c6 77 68 67 25 ae fd 99 00 6e 2e 53 e6 60 50 50 ae a8 0f 9b 0a"
ct = bytes.fromhex(ct_hex)
with open("/usr/share/wordlists/rockyou.txt", "r", encoding="utf8", errors="ignore") as f:
    lines = f.readlines()

pattern = re.compile("^[A-Z]+")
for line in tqdm(lines):
    l = line.rstrip().upper()
    if pattern.match(l):
        key = l.encode()
        cipher = ARC4.new(key)
        pt = cipher.decrypt(ct)
        if pt.startswith(b"poctf{uwsp_"):
            print(f"Key: {key}")
            print(f"Plaintext: {pt}")
            exit(0)
