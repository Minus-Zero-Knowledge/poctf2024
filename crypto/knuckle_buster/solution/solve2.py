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
