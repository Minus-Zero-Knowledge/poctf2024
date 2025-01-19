iv_hex = "437261636b3430302d58"
iv = iv_hex[:32] if len(iv_hex) >= 32 else iv_hex.ljust(32, "0")
iv_bytes = bytes.fromhex(iv)

print(iv_bytes)   # b'Crack400-X\x00\x00\x00\x00\x00\x00'