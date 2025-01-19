from Crypto.Util.number import long_to_bytes

with open("../public/Stego100-2.txt", "rb") as f:
    bts = f.read(4096)

filtered = []
for i in range(len(bts)):
    match bts[i:i+1]:
        case b'\x8b':
            filtered.append('1')
        case b'\x8c':
            filtered.append('0')

a = int("".join(filtered), 2)
print(long_to_bytes(a))
