with open('ftp_data1', 'rb') as f:
    data1 = f.read()

with open('ftp_data2', 'rb') as f:
    data2 = f.read()

with open('out.jpg', 'wb') as f:
    result = bytearray(data1)
    # replace the first part of data1 with the bytes from data2
    result[0:len(data2)] = data2

    # fix the wrong header (0xdeadbeef) in the result using the correct magic bytes for a JFIF
    jfif_magic_bytes = bytes.fromhex("ff d8 ff e0")
    result[0:len(jfif_magic_bytes)] = jfif_magic_bytes

    f.write(result)
