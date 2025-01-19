# Reverse 300-2 - Think Different Be Similar
## Description
Honestly, I thought this one might be too easy for a 300-level challenge, but I ultimately decided to go for it. What we have here is a very simple application that actually does the work for you. When you run it, it will fetch the flag for you and let you know if it succeeded or not. It would, obviously, be much more handy if it actually displayed the flag, but that's just a little technicality for someone with your skills.

Right Click, Save As... [Descriptive Derscription](https://pointeroverflowctf.com/static/Reverse300-2.exe)

MD5 checksum 935FA5EFF8BF6F7D8D4B0FC52E1D68B1

## Solution
Intercept the traffic while running the binary (e.g. `Fiddler` or `wireshark`).

Following request is made:

```
GET http://nvstgt.com/ThinkDifferentBeSimilar/poctf2024_reverse3002.txt HTTP/1.1
Host: nvstgt.com
User-Agent: ThinkDifferentBeSimilar
Referer: https://www.nvstgt.com/
```

with the following response:
```
HTTP/1.1 200 OK
Server: openresty/1.21.4.1
Date: Mon, 25 Nov 2024 20:07:48 GMT
Content-Type: text/plain
Content-Length: 28
Connection: keep-alive
Vary: User-Agent
Last-Modified: Sat, 23 Nov 2024 10:54:13 GMT
ETag: "1c-6279251f29fc1"
Accept-Ranges: bytes
Cache-Control: max-age=604800
Expires: Mon, 02 Dec 2024 20:07:48 GMT
Strict-Transport-Security: max-age=0;

poctf{uwsp_4b4nd0n_4ll_h0p3}
```
## Flag
`poctf{uwsp_4b4nd0n_4ll_h0p3}`
