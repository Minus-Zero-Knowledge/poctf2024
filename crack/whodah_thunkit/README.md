# Crack 300-3 - Whodah Thunkit
## Description
Time to dust off rockyou! For this challenge you will be taking on a little application I'm considering selling to some major security firm. I'm considering pitching to CrowdStrike, but I might also see if I can find a number for Fortinet. Test it out for yourself and you'll see how it's going to revolutionize the cybersecurity industry! Well, if I can ever get it to work anyway. See, it's really more of an idea than a real thing.

The target below is running my app. When you connect to the target it will prompt you for a password. Sounds like an exploit challenge, right? Well, there's another path. Follow the rules and develop a solution to crack the password and the program will give give you the flag.

Your target is our target is 34.123.210.162 on port 32320

## Solution
The goal is to find the correct hash. 

There are 2 ways: 
1) Either use `rockyou` and calculate the hash according to the procedure 1. Base64 encode 2. Reverse 3. md5sum. This will yield **yougotserved** as the correct password.
2) Another way is through the `help` interface. It gives the number of correct characters and the number of characters in correct positions. This can be leveraged to find each character of the hash one by one.

## Flag
`poctf{uwsp_l0n3ly_4nd_f0r70rn}`
