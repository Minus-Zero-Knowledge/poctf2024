# DF 300-3 - I'm a Stranger Here Myself
## Description
I was inspired to create this challenge after a real case I worked. In my experience, actual steganography is pretty rare and typically signifies a subject with advanced domain competency in counter-forensics. Most subjects will use encryption or basic obfuscation because you get similar results with less hassle. Only the most sensitive of evidence and most paranoid of subjects encrypt and hide their data.

I was contacted to reexamine evidence in a criminal case. It was an alleged criminal conspiracy with multiple subjects. Five, to be exact, and it was suspected that there was a sixth. The only problem was that there was no solid evidence directly linking this sixth member to the conspiracy. I took a look and discovered a situation that is crudely reproduced in this challenge.

NOTE: The flag for this challenge uses a '1' in place of both the 'i' and 'l' characters. You can submit the flag as found, or using the character set in the rules. Either will be accepted. 

Right Click, Save As... [DF300 Pcap](https://pointeroverflowctf.com/static/DF300-3.pcap)

## Solution
There are two FTP data streams in the pcap. These can be extracted by `Follow > TCP Stream > Raw > Save as` in `wireshark`. 
The first FTP data does not seem to have a header while the second seems to be only the header of a JFIF file. 
We therefore replace the first 256 bytes of the first data source by the second. We now see that the first four bytes are `DEADBEEF`. These are not the correct magic bytes for a JFIF file. Changing these to the correct bytes (`FF D8 FF E0`) gives an image which reveals the flag.

## Flag
`poctf{uwsp_f34r_15_7h3_m1nd_k1113r}`
