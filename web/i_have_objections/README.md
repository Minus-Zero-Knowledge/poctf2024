# Web 100-2 - I Have Objections
## Description
Ok, I'm a little nervous about this one. It seemed like a good idea when I came up with it and I suppose it's too late to back out now... This next challenge will involve compromising a live stream site and to make sure it's as real as possible, I've set up a camera and will be broadcasting LIVE 24/7 until the end of the contest! Join right away, and you'll be treated to a little behind-the-scenes walk-through of Prof Johnson's lab and while you're there see if you can find the flag!

NOTE: Since this is a 100-level challenge, let me save you a little time: /flag 

[I'm Ready for my Close Up, Mr. Demille](http://34.135.223.176:8449/)

[Don't Worry, It's an Old Reference, Even for Me](https://www.youtube.com/watch?v=TVi1NlYBljU)

## Solution
Use `{{7*7}}` as payload for the `/complaint` endpoint. Observe that the result is 49, meaning that the server is vulnerable to a SSTI attack. The server seems to use `Jinja2`. From https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection, we can then use RCE payloads such as `{{ cycler.__init__.__globals__.os.popen('id').read() }}`. After using `ls -la` first to list the files on the server, we then do `cat app.py`. The result is in `solution/app.py`. 
The flag is visible in the source code (and shows an easier solution using an `XMLHttpRequest`).

## Flag
`poctf{uwsp_71m3_15_4n_1llu510n}`
