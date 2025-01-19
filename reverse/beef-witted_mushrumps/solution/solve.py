from pwn import xor
encoded = b"p\037|\bn\025`\027d\024K|\024'x\037+Fu*\033.qE#\023#\024i"
print(xor(encoded[1:], encoded[:-1]))
