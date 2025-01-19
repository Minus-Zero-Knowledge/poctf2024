# Web 400 - A Bitter Delicacy
## Description
We're getting closer and closer to the end of Pointer Overflow 2022 and it's time for me to start tipping my hand, sharing those hidden secrets, and releasing the last few 400-level challenges that remain. This one requires access to some really high-end gear.

I know, I know... One of the contest axioms is that the challenges should be solvable with cleverness and skill and not good gear. Well, I'm going to give you access to my person botnet for this one, so you should have all you need. Just be responsible with it!

To make sure you don't get up to any mischief I've hidden the login page to the admin console, have an error.log running in a secure location a level higher than the app, and I've hidden all other sensitive information using cutting-edge Linux methods (the OS hackers and the NSA use, look it up.) If you want to want to solve this one, it will require discovering a couple secrets and paying close attention to what you know so you can work out what you don't know.

[I Was Kidding the Password is Not Password123!](http://34.135.223.176:10404/)

## Solution
First fuzz the correct directory: `http://34.135.223.176:10404/view-file?file=.hidden`

The flag file is found at `http://34.135.223.176:10404/view-file?file=.hidden/flag.txt`

## Flag
`poctf{uwsp_4ll_w3_h4v3_70_d3c1d3}`
