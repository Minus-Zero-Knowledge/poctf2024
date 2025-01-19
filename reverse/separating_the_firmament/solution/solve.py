from pwn import process
p = process('../public/Reverse300-1')
p.sendline(b'dchfwREaguPJ8!pV*^U&Ms')
p.interactive()

# poctf{uwsp_7h3_w0rld_15_4_57463}