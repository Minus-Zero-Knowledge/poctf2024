from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from pwn import xor

s2_hex = "fa21c9c2596099915dbc7845c941c14e81594b5c4f69177cc4059da11e782e0b"
key_hex = "504f43544632303234"
iv_hex = "437261636b3430302d58"
key_bytes = bytes.fromhex(key_hex).ljust(16, b'\x00')
iv_bytes = bytes.fromhex(iv_hex).ljust(16, b'\x00')

def right_rotate(byte, num_bits):
    arr = bin(byte)[2:].zfill(8)
    return int(arr[-num_bits:] + arr[:-num_bits], 2)

def rev_custom_transform(data, key_bytes, iv_bytes):
    key_length = len(key_bytes)
    iv_length = len(iv_bytes)
    transformed = bytearray()

    for index, byte in enumerate(data):
        rotation = (key_bytes[index % key_length] + iv_bytes[index % iv_length]) % 8
        transformed.append(right_rotate(byte, rotation))

    return transformed

def aes_decrypt(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data), cipher.block_size)

print("Decrypted flag:", dec := aes_decrypt(bytes.fromhex(s2_hex), key_bytes, iv_bytes))
print(rev := rev_custom_transform(dec, key_bytes, iv_bytes))
print(xor(42, rev))
