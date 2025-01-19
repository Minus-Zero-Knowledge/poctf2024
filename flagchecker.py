import re
import argparse

plaintext_alphabet = "abcdefghijklmnopqrstuvwxyz "
flag_alphabet = "4bcd3f6h1jklmn0pqr57uvwxyz_"

flag_regex = re.compile(r"poctf\{uwsp_(.+)}", re.IGNORECASE)

parser = argparse.ArgumentParser(
    prog='pointeroverflow flag util',
    description='encodes/decodes pointeroverflow ctf flags')

parser.add_argument("flag", type=str)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-e", "--encode", action="store_true")
group.add_argument("-d", "--decode", action="store_true")

args = parser.parse_args()

encoder = str.maketrans(plaintext_alphabet, flag_alphabet)
decoder = str.maketrans(flag_alphabet, plaintext_alphabet)


def encode(s: str) -> str:
    translated = s.translate(encoder)
    return f"poctf{{uwsp_{translated}}}"


def decode(s: str) -> (str, bool):
    if m := flag_regex.match(s):
        txt = m.group(1).lower()
        alphabet_errors = any(c not in flag_alphabet for c in txt)
        return txt.translate(decoder), alphabet_errors
    else:
        return s.translate(decoder), True


def main():
    if args.encode:
        print(encode(args.flag))

    elif args.decode:
        res, alphabet_errors = decode(args.flag)
        print(res)
        if alphabet_errors:
            print("warning: flag does not conform to standard format")


if __name__ == "__main__":
    main()
