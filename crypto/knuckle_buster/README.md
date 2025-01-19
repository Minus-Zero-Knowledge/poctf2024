# Crypto 200-1 - Knuckle Buster
## Description
In this challenge, two individuals—Alice and Bob—are communicating in secret. They use the Diffie-Hellman key exchange protocol to protect their communication. I will provide you with enough information to decrypt a message intercepted between them. All you need to do is calculate the shared secret and decrypt it to get the flag.

Here is the encrypted flag. It was encrypted using AES-256-CBC, with SHA-256 for key derivation and a prepended 16 byte IV.

publicA
-----BEGIN PUBLIC KEY-----
MIGaMFMGCSqGSIb3DQEDATBGAkEAiBB/FlC3W8aPLJxYGXzKsnpEmPKIKR4JetlA1ky+TKTYofXUKSFucGxtrmWlVFjnLZUqJFjj0bVDKSiYOfod1wIBAgNDAAJAN3YrjXtIssyugO9tQ3BRy2TN92Qkhkp/VP5zfLEMQg1AE/YofkCIc/KSZOBpuroiQoCK0qTNkD4HzCzDa7ap5Q==
-----END PUBLIC KEY-----

privateB
-----BEGIN PRIVATE KEY-----
MIGcAgEAMFMGCSqGSIb3DQEDATBGAkEAiBB/FlC3W8aPLJxYGXzKsnpEmPKIKR4JetlA1ky+TKTYofXUKSFucGxtrmWlVFjnLZUqJFjj0bVDKSiYOfod1wIBAgRCAkBSsgvp3xivPK6Wp2X+SIjGllg1MT4zJdEoyUjV6iDLGytdeLpokYOO6xsGIiVb8b6A/5onnopra2iXBb0dS5rn
-----END PRIVATE KEY-----

dhparam
-----BEGIN DH PARAMETERS-----
MEYCQQCIEH8WULdbxo8snFgZfMqyekSY8ogpHgl62UDWTL5MpNih9dQpIW5wbG2uZaVUWOctlSokWOPRtUMpKJg5+h3XAgEC
-----END DH PARAMETERS-----

Right Click, Save As.... [Encrypted Flag](https://pointeroverflowctf.com/static/Crypto200-1_flag.txt.enc)


## Solution
```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

# Load public key from Alice
with open("../public/publicA.pem", "rb") as f:
    publicA = load_pem_public_key(f.read())

# Load private key from Bob
with open("../public/privateB.pem", "rb") as f:
    privateB = load_pem_private_key(f.read(), password=None)

# Load DH parameters
with open("../public/dhparam.pem", "rb") as f:
    dh_params = serialization.load_pem_parameters(f.read())

# Generate the shared secret
shared_secret = privateB.exchange(publicA)

# Derive the AES-256 key from the shared secret
digest = hashes.Hash(hashes.SHA256())
digest.update(shared_secret)
aes_key = digest.finalize()  # our 32-byte AES-256 key

# Read the encrypted file (16-byte IV followed by ciphertext)
with open("../public/Crypto200-1_flag.txt.enc", "rb") as f:
    iv = f.read(16)         # AES CBC IV
    ciphertext = f.read()   # Encrypted message content

# Decrypt the ciphertext using AES-256-CBC
cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
decryptor = cipher.decryptor()
decrypted_flag = decryptor.update(ciphertext) + decryptor.finalize()

# Print the decrypted flag
print(f"Decrypted Flag: {decrypted_flag}")
```


## Flag
`poctf{uwsp_f1r3_4nd_br1m570n3}`