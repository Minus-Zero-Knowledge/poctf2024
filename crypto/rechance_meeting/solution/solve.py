import hashlib
from tqdm import tqdm

def custom_hash(input_str):
    sha256_hash = hashlib.sha256(input_str.encode()).hexdigest()
    md5_hash = hashlib.md5(input_str.encode()).hexdigest()
    
    combined_hash = sha256_hash + md5_hash
    
    hash_value1 = 0
    hash_value2 = 0
    hash_value3 = 0
    
    primes = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    
    for i, char in enumerate(combined_hash):
        hash_value1 += (i + 1) * ord(char) * primes[i % len(primes)]
        hash_value1 ^= (ord(char) << (i % 8))
        hash_value1 += (ord(char) ** 3) * primes[(i + 1) % len(primes)]
        hash_value1 ^= (ord(char) * 53) * (i + 1) * primes[(i + 2) % len(primes)]
        
        hash_value2 += (i + 1) * ord(char) * primes[(i + 3) % len(primes)]
        hash_value2 ^= (ord(char) << ((i + 3) % 8))
        hash_value2 += (ord(char) ** 2) * primes[(i + 4) % len(primes)]
        hash_value2 ^= (ord(char) * 29) * (i + 2) * primes[(i + 5) % len(primes)]
        
        hash_value3 += (i + 1) * ord(char) * primes[(i + 5) % len(primes)]
        hash_value3 ^= (ord(char) << ((i + 6) % 8))
        hash_value3 += (ord(char) ** 4) * primes[(i + 7) % len(primes)]
        hash_value3 ^= (ord(char) * 19) * (i + 3) * primes[(i + 8) % len(primes)]
    
    combined_hash_value = (hash_value1 + hash_value2 + hash_value3) * 31
    combined_hash_value ^= (combined_hash_value << 13)
    combined_hash_value += (combined_hash_value >> 17)
    combined_hash_value ^= (combined_hash_value << 5)
    
    return combined_hash_value % 999999937

def derive_key(input1, input2):
    combined = input1 + input2
    key = hashlib.sha256(combined.encode()).hexdigest()
    return key

def find_collisions():
    with open("../public/Crypto200-2_words.txt", "r") as f:
        lines = f.readlines()

    hashes = {}
    collisions = []
    for line in tqdm(lines):
        word = line.strip()
        hsh = custom_hash(word)
        if hsh in hashes:
            for hsh2 in hashes[hsh]:
                collisions.append((word, hsh2))
                collisions.append((hsh2, word))
            print(word, hashes[hsh])
            hashes[hsh] += [word]
        else:
            hashes[hsh] = [word]
    return collisions


import pyzipper

def main():
    collisions = find_collisions()
    with pyzipper.AESZipFile("../public/Crypto200-2_flag.zip", "r") as zf:
        for x, y in collisions:
            pw = f"{x}{y}".encode()
            try:
                zf.extract("Crypto 200-2 flag.txt", "./output", pwd=pw)
                print(pw, "found")
                break
            except RuntimeError as e:
                print(e, pw)

    # poctf{uwsp_w3_c4n_r3m3mb3r_17}


if __name__ == "__main__":
    main()
