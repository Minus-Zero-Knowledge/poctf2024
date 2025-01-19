from pwn import xor

ct = bytes.fromhex('8a258a3a8a368a218a338a2e8a208a228a268a258a0a8a238a618a648a398a0a8a658a338a0a8a648a328a3b8a658a278a618a3b8a368a668a28')
print(xor(ct, b'U')[1::2])