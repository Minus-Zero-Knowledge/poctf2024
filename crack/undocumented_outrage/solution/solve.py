import msoffcrypto

with open("../public/Crack200-2.docx", "rb") as encrypted:
    file = msoffcrypto.OfficeFile(encrypted)
    password = "холоднокатаного"
    file.load_key(password=password, verify_password=True)
    with open("decrypted.docx", "wb") as decrypted:
        file.decrypt(decrypted)
