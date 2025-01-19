import wave
import struct
from typing import Iterator, Tuple
from itertools import groupby

def run_length_encode(data: str) -> Iterator[Tuple[str, int]]:
    """Returns run length encoded Tuples for string"""
    # A memory efficient (lazy) and pythonic solution using generators
    return ((x, sum(1 for _ in y)) for x, y in groupby(data))

wav = wave.open("../public/track2", mode='rb')
print(wav.getparams())
frame_bytes = bytearray(list(wav.readframes(wav.getnframes())))
shorts = struct.unpack('H'*(len(frame_bytes)//2), frame_bytes)
bits = []

i = 0
while i < len(shorts):
    hx = hex(shorts[i])[2:]
    a = hx.zfill(4)
    if shorts[i] < 30000: # low or high
        bits.append(0)
    else:
        bits.append(1)
    i += 1

j = 0
for a, b in run_length_encode(bits):
    print(a, b)
    j += 1
    if j > 1000:
        break
