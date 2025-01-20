# Crack 200-1 - Now You See Me 
## Description
Another Crack challenge, and I'm going to make this tricky by giving you a series of cryptic clues, then it'll be up to you to work your magick and find the flag. Here are two images. One is a key. The other you can't see because it's encrypted, but it's the flag. 

![Crack200-1key.png](public/Crack200-1key.png)
MD5 checksum 0AA46A2867C4339EBDBC4955B3BD237D 

![Crack200-1flag.png](public/Crack200-1flag.png)
MD5 checksum B9DFD8F6D8101A2C32B5C28277B43CB5

Ok. Here are your clues:
1) [A-Z0-9]{10}
2) The password is somewhere in this text.

X3G7B9J2LQM5K8N1T4ZVP0D2S9C6JHF7Y3L8M1QWH4J6K2Z8N9Q9L1T3D6X2A8S5F2G7H1B3C6D9E2R4N0M5L7K3J8V6W2E4R8Y1U1I2O3P4A5S9D8F7G6H5T4Y3U2I1O0E6R5T4Y3U2G7H8J9K0L1Z3X4C5V6B7M8N7B6V5C4L2K3J4H5G6F1D2S3A4Q5W6E7R8T9Y0U9I8O7P6A5S4D3F2G1H0J9K8L7M6N5B4V3C2X1Z0A1S2D3F4G5H6J7K8L9M0N1B2V3C4X5Z6A7S8D9F0G1H2J3K4L5M6N7B8V9C0X1Z2A3S4D5F6G7H8J9K0L1M2N3B4V5C6X7Z8A9S0D1F2G3H4J5K6L7M8N9B0V1C2X3Z4A5S6D7F8G9H0J1K2L3M4N5B6V7C8X9Z0A1S2D3F4G5H6J7K8L9M0N1B2V3C4X5Z6A7S8D9F0G1H2J3K4L5M6N7B8V9C0X1Z2A3S4D5F6G7H8J9K0L1M2N3B4V5C6X7Z8A9S0D1F2G3H4J5K6L7M8N9B0V1C2X3Z4A5S6D7F8G9H0J1K2L3M4N5B6V7C8X9Z0A2S3D4F5G6H7J8K9L0M1N2B3V4C5X6Z7A8S9D0F1G2H3J4K5L6M7N8B9V0C1X2Z3A4S5D6F7G8H9J0K1L2M3N4B5V6C7X8Z9A0S1D2F3G4H5J6K7L8M9N0B1V2C3X4Z5A6S7D8F9G0H1J2K3L4M5N6B7V8C9X0Z1A3S4D5F6G7H8J9K0L1M2N3B4V5C6X7Z8A9S0D1F2G3H4J5K6L7M8N9B0V1C2X3Z4A5S6D7F8G9H0J1K2L3M4N5B6V7C9X0Z1A2S3D4F5G6H7J8K9L0M1N2B3V4C5X6Z7A8S9D0F1G2H3J4K5L6M7N8B8V9C0X1Z2A4S5D6F7G8H9J0K1L2M3N4B5V6C7X8Z9A0S1D2F3G4H5J6K7L8M9N0B1V2C3X4Z5A6S7D8F9G0H1J2K3L4M5N6B7V8C9X0Z1A2S3D4F5G6H7J8K9L0M1N2B3V4C5X6Z7A8S9D0F1G2H3J4K5L6M7N8

## Solution
Collect **all** the strings in the ___complete___ description matching the regex `[A-Z0-9]{10}`. This includes the MD5 checksums of the images.

The description hints that the flag image is encrypted using ImageMagick.
Running the command `printf "0AA46A2867" | ./magick ../public/Crack200-1flag.png -decipher - decrypted` results in the correct decrypted image.
(Sidenote: do not simply use `echo` as this adds a trailing newline character; use `printf` or `echo -n`.)

![0000_0AA46A2867.png](solution/0AA46A2867.png)

An alternative approach is to use the fact that the nonce is calculated deterministically [based on the first half of the password and some image metadata](https://imagemagick.org/script/cipher.php). 
This allows for testing all passwords of the form `XXXXXAAAAA` where `XXXXX` iterates over all strings in the set `[A-Z0-9]{5}` (note that the nonce is present in the metadata) to obtain the first half of the password. The rest of the password can then be easily brute-forced for a total iteration complexity of $2\cdot 36^5$ tries. This approach was too slow in `Python` but can be done faster in `C` by performing the nonce brute-force in the ImageMagick internals itself.

## Flag
`poctf{uwsp_Unbr34k4bl3_Ch41n}`
