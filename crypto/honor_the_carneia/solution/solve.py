import requests
import json
from pwn import xor

ciphertext = "f51f3527f214ff5a96611ace79fc24efbecd2f7ae65bf6a853c8fb95f7200fd5bd4aca6c5899b1923c9c288b023929f0"
ciphertext = bytes.fromhex(ciphertext)


def oracle(ct):
    r = requests.post('http://34.123.210.162:5003/padding_oracle', json={'ciphertext': ct.hex()})
    if r.status_code == 200:
        return json.loads(r.text)['valid_padding']

    print("too fast")
    return -2


# decrypt a single block as an ECB decrypt oracle using a padding oracle
def decrypt_block(block):
    decrypted = bytearray(16)
    iv = bytearray(16)
    for bt in range(15, -1, -1):
        print(bt)
        print(decrypted)
        # set up tailing iv such that it contains 0x02; 0x03, 0x03; 0x04, 0x04, 0x04
        # and so on, depending on the current byte to be found
        target_bt = 16 - bt
        for k in range(bt + 1, 16):
            iv[k] = target_bt ^ decrypted[k]

        # find iv value which leads to correct padding
        for c in range(256):
            iv[bt] = c
            correct_pad = oracle(iv + block)
            if correct_pad:
                # change preceding byte to disambiguate
                if bt != 0:
                    iv[bt - 1] = 123
                if oracle(iv + block):
                    decrypted[bt] = c ^ target_bt
                    break
    return decrypted


blocks = []
ct = ciphertext
for i in range(0, len(ct), 16):
    blocks.append(ct[i:i + 16])

message = bytearray()
for block in range(1, len(blocks)):
    message += decrypt_block(blocks[block])

message[:16] = xor(message[0:16], blocks[0])
message[16:] = xor(message[16:], blocks[1])
print(message)
