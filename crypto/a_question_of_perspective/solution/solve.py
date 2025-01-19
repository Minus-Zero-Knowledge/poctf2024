from pwn import xor
from Crypto.Util.number import bytes_to_long, long_to_bytes
import itertools

Qubits = [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1]
Bases = ['R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'D', 'D', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 'R', 'D', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'D', 'R', 'D', 'D', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'D', 'R', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 'D', 'D']
crack_hint = int(''.join(str(x) for x in Qubits), 2)
print(long_to_bytes(crack_hint))

Enc = [0x23, 0x59, 0x86, 0x1e, 0x60, 0xcf, 0xdc, 0x4e, 0x6a, 0x0b, 0x0c, 0x50, 0xd4, 0x5a, 0x71, 0x87, 0xdb, 0x0c, 0x46, 0x1d, 0x63, 0x44, 0xba, 0x5e, 0x37, 0xd3, 0x9a, 0x4b, 0x77, 0x4b, 0x3d, 0x4b]
key = bin(bytes_to_long(xor(Enc, b'poctf{')))[2:].zfill(len(Enc) * 8)
Measurements = [0, 1, None, 1, 0, None, 1, 1, None, 0, 1, None, 0, 1, None, 0, 1, None, 1, 0, None, 1, 0, None, 0, 1, None, 0, 1, None, 1, 0, None, 0, 0, None, 0, 1, None, 0, 1, None, 1, 1, None, 1, 0, None, 1, 0, None, 0, 1, None, 0, 1, None, 0, 1, None, 1, 0, None, 1, 0, None, 0, 1, None, 0, 0, None, 0, 1, None, 1, 1, None, 1, 1] 
for i in range(48):
    if Measurements[i] is None:
        Measurements[i] = int(key[i])
    else:
        if Measurements[i] != int(key[i]):
            print('wrong', Measurements[i], key[i], i)

Nones = sum(1 if i is None else 0 for i in Measurements)
Indices = [i for i in range(len(Measurements)) if Measurements[i] is None]
for ch in itertools.product([0,1], repeat=Nones):
    for k, i in enumerate(Indices):
        Measurements[i] = ch[k]
    key = int(''.join(str(x) for x in Measurements), 2)
    dec = xor(Enc, long_to_bytes(key))
    if dec.startswith(b'poctf{uwsp_') and dec.endswith(b'}'):
        print(dec)

