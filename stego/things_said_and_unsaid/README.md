# Stego 100-3 - Things Said and Unsaid
## Description
So there I was connected to the free McDonald's Wi-Fi hackin' the ISS nav computer as it passed by from orbit and I intercepted a still image from one of the onboard camera feeds. Something about it just seems a little odd, but I can't quite place it... Then again, it might just be my face-blindness acting up!

Remember, this is a Stego challenge. A password will be required to solve the challenge, and that means the password will also be hidden somewhere in the challenge.


# Solution
```
strings Stego100-3.jpeg  -> 'probably unprobable'
binwalk -e Stego100-3.jpeg
```
Extract zip file with password **probably unprobable**.

## Flag
`poctf{uwsp_w3_4r3_such_57uff}`
