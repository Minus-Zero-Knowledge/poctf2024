# Crack 300-2 - Return of the Mack
## Description

Sterling Archer. Code name: Duchess. Known from Berlin to Bangkok as the world's most dangerous spy. So, for us, this is... How you say? A good get. But not so good for you, Mr. Archer. Because you have information that I want. And this may be an old cliche but... We have ways of making you talk.

The message below was recovered from Sealab's master computer in 2021. We know that it is a secret transmission between Mr. Reed and Dr. P. Haze. We also know that you know the code to this private key to decrypt it. You will give us that code. No games, Archer, 6 characters, A-Z and 0-9 only.

Right Click, Save As... [Encrypted Message](https://pointeroverflowctf.com/static/Crack300-2_flag.txt.enc)

MD5 checksum 81EBBB5BBEC7049980850F84957E060E

Right Click, Save As... [Private Key](https://pointeroverflowctf.com/static/Crack300-2.pem)

MD5 checksum 01C257F8955C360196235EFDE6097E77


## Solution
Extract the hash using `pem2john.py` (warning: there are multiple versions and all of them seem to contain bugs and the result needs manual correcting).

The pem file can be parsed with an ASN.1 parser (e.g. https://lapo.it/asn1js/) to verify the format: PKCS#8 Private Keys (PBKDF2-HMAC-SHA256 + 3DES/AES). 
The hash must start with `$PEM$2$4$` in order to work with [hash mode 24420](https://hashcat.net/wiki/doku.php?id=example_hashes).

After specifying a mask file corresponding to 6 uppercase letters and/or digits: `?u?d,?1?1?1?1?1?1`, we crack the password using `hashcat` as **934TXS**.
Decoding the encrypted file reveals the plaintext file: ```openssl pkeyutl -decrypt -in Crack300-2_flag.txt.enc -out Crack300-2_flag.txt -inkey Crack300-2.pem -passin pass:934TXS```


## Flag
`poctf{uwsp_h34r7_0f_7h3_m4773r}`
