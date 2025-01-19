from pwn import *

context.log_level = 'debug'

r = remote('34.123.210.162', 32320)
r.sendline(b'help')
current_password = ''

def query(s):
    r.sendline(s)
    r.recvuntil(b'Try again.')
    r.recvline()
    output = r.recvline().decode()
    output = output.split()
    num_match = int(output[0])
    num_correct = int(output[6])
    return num_correct

alphabet = 'abcdef0123456789'
for pos in range(32):
    best = 0
    best_char = '#'
    for c in alphabet:
        curr = current_password + c + 'a' * (32 - pos - 1)
        correct = query(curr)

        if correct > best:
            best = correct
            best_char = c
    current_password += best_char
    print(current_password)
r.interactive()

# aac56acc457c9cf0f15ad8d20347b7aa
# poctf{uwsp_l0n3ly_4nd_f0r70rn}