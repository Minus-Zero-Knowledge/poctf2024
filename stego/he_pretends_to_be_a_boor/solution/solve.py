import numpy as np
import jpegio as jio

# Load the JPEG image
jpeg_img = jio.read('../public/Stego400.jpg')

# Extract and print the quantization tables (DQT)
for idx, dqt_table in enumerate(jpeg_img.quant_tables):
    print(f"Quantization Table {idx}:")
    print(dqt_table)

# Decode the values of the first quantization table
values = []
for arr in jpeg_img.quant_tables[0]:
    for val in arr:
        values.append(val)

print("".join(chr(x) for x in values))
