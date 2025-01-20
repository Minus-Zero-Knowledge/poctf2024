# DF 200-1 - Hooper Hollar 
## Description
Learning memory forensics, as I recall, was a painful process. Not because it was difficult, but because when it was difficult it was very difficult, and when it wasn't it was very easy. I'd find myself over-thinking things a lot. Mapping out memory and taking copious notes when the truth was right there for the taking if I'd just thought to look before diving in. 

Right Click, Save As... [If You Don't, Remember Me](https://uwspedu-my.sharepoint.com/:u:/g/personal/cjohnson_uwsp_edu/EU0BFDviyvRPjVo5KIRfamYBA0ipJHNOYF3k6A5elJWfHA?e=pBwhsn)

MD5 checksum CE7C8C5609F34561860CEFA19F87DCDE

Alternate Link... [Direct Download](https://pointeroverflowctf.com/static/DF200-1.mem)

## Solution
```
$ file DF200-1.mem 
DF200-1.mem: Windows Event Trace Log
```

`strings DF200-1.mem | grep poctf{uwsp_`

## Flag
`poctf{uwsp_l3553r_b31ng5}`
