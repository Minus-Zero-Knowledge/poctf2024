enc_flag = "2d383c313f2432302c2d08710870356e376f086d3f083b6c713270262a"
enc_flag = bytes.fromhex(enc_flag)
dec_flag = [chr((i - 3) ^ 0x5a) for i in enc_flag]

print("".join(dec_flag))