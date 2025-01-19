import hashlib
from Crypto.Cipher import AES

p = int('88107F1650B75BC68F2C9C58197CCAB27A4498F288291E097AD940D64CBE4CA4D8A1F5D429216E706C6DAE65A55458E72D952A2458E3D1B54329289839FA1DD7', 16)
g = 2

alice_pub = int('''37:76:2b:8d:7b:48:b2:cc:ae:80:ef:6d:43:70:51:
    cb:64:cd:f7:64:24:86:4a:7f:54:fe:73:7c:b1:0c:
    42:0d:40:13:f6:28:7e:40:88:73:f2:92:64:e0:69:
    ba:ba:22:42:80:8a:d2:a4:cd:90:3e:07:cc:2c:c3:
    6b:b6:a9:e5'''.replace('\n', '').replace(':', ''). replace(' ', ''), 16)
bob_priv = int('''52:b2:0b:e9:df:18:af:3c:ae:96:a7:65:fe:48:88:
    c6:96:58:35:31:3e:33:25:d1:28:c9:48:d5:ea:20:
    cb:1b:2b:5d:78:ba:68:91:83:8e:eb:1b:06:22:25:
    5b:f1:be:80:ff:9a:27:9e:8a:6b:6b:68:97:05:bd:
    1d:4b:9a:e7'''.replace('\n', '').replace(':', '').replace(' ', ''), 16)
bob_pub = int('''5a:5c:cd:22:1c:2e:f7:f0:16:6e:f9:70:17:c3:ce:
    11:ff:1c:b6:f0:d3:98:41:ff:23:f7:f0:3c:41:27:
    7d:bd:da:64:ad:db:da:5a:b8:51:67:9f:94:17:34:
    d1:37:1e:79:20:de:44:95:5f:54:bd:a8:76:aa:08:
    df:2c:f4:30'''.replace('\n', '').replace(':', '').replace(' ', ''), 16)

shared_secret = pow(alice_pub, bob_priv, p)
print(shared_secret)
sha = hashlib.sha256()
sha.update(bytes.fromhex(hex(shared_secret)[2:]))
key = sha.digest()
with open('../public/Crypto200-1_flag.txt.enc', 'rb') as f:
    ct = f.read(256)

print(key.hex())
iv = ct[:16]
ct = ct[16:]
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ct)
print(plaintext)