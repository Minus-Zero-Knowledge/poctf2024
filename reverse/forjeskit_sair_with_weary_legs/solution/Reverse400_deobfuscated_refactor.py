from Crypto.Cipher import AES as AES
from Crypto.Util.Padding import pad as pad


def xor_42(s: str) -> str:
    return "".join(chr(ord(x) ^ 42) for x in s)


def left_rotate(byte: int, num_bits: int) -> int:
    return byte << num_bits & 255 | byte >> 8 - num_bits


def custom_transform(data, key_bytes, iv_bytes):
    key_length = len(key_bytes)
    iv_length = len(iv_bytes)
    transformed = bytearray()

    for index, byte in enumerate(data):
        rotation = (key_bytes[index % key_length] + iv_bytes[index % iv_length]) % 8
        transformed.append(left_rotate(byte, rotation))

    return transformed


# AES encryption wrapper
def aes_encrypt(data, key: bytes, iv: bytes):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(data, AES.block_size))


def bytes_from_hex(hex_s: str) -> bytes:
    return bytes.fromhex(hex_s)


s1 = "[redacted]"

s2_hex = "fa21c9c2596099915dbc7845c941c14e81594b5c4f69177cc4059da11e782e0b"

key_hex = "504f43544632303234"

iv_hex = "437261636b3430302d58"

xor_output = xor_42(s1)

key_bytes = bytes_from_hex(key_hex)

if len(key_bytes) < 16:
    key_bytes = key_bytes.ljust(16, b"\x00")

iv = iv_hex[:32] if len(iv_hex) >= 32 else iv_hex.ljust(32, "0")

iv_bytes = bytes.fromhex(iv)

data = custom_transform(xor_output.encode("utf-8"), key_bytes, iv_bytes)

flag_enc = aes_encrypt(data, key_bytes, iv_bytes)

print("Encrypted flag:", flag_enc.hex())
#Encrypted flag: bd7e9dad4a5fe0e7911f93cb1bf5a321
__import__("sys").exit()
