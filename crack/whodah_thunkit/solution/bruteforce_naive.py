from pwn import *
import hashlib
import base64
import tqdm
from datetime import datetime

def transform(password: str) -> str:
    encoded = base64.b64encode(password.encode())[::-1]
    result = hashlib.md5(encoded).hexdigest()

    return result

#context.log_level = 'debug'

def main():
    start_time = datetime.now()
    print(start_time)

    r = remote('34.123.210.162', 32320)
    r.recvline_startswith(b"Enter the password")
    with open("/usr/share/wordlists/rockyou.txt", "r") as f:
        for l in tqdm.tqdm(f):
            pwd = l.rstrip()
            result = transform(pwd)
            r.sendline(result.encode())
            l = r.recvline()
            if l.startswith(b"Incorrect password"):
                _ = r.recvline()
                continue
            else:
                print(l)
                print(r.clean())
                print(pwd, result)
                break

    end_time = datetime.now()
    print(end_time)

if __name__ == "__main__":
    main()


# yougotserved aac56acc457c9cf0f15ad8d20347b7aa
# poctf{uwsp_l0n3ly_4nd_f0r70rn}