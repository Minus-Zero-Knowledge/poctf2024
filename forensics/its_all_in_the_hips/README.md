# DF 300-1 - It's All in the Hips 
## Description
Somehow, I've ended up with a collection of security cameras. Mostly from POCs. You know, working on security you sometimes vet physical security systems. Particularly if they have large IT requirements and deal with potentially sensitive data. Well, because they're never in service I just sort-of keep them laying around. However, I came in after break one morning and noticed one of the cameras was not in it usual place. Suspecting a set-up (I am always wary of people trying to grass me up) I examined the camera. What I found was astounding. Seems the camera went on quite an adventure in the night. Not sure who's responsible, but t seems they had fun.

Right Click, Save As... [Baby, You've Got a Stew Going](https://pointeroverflowctf.com/static/DF300-1.001)

Alternate Link... [Baby, You've Got a Stew Going](https://uwspedu-my.sharepoint.com/:u:/g/personal/cjohnson_uwsp_edu/EYNqFUXg7F5Kp2oyuM0_FtoBJGPoVKE64i4PuVffV7EGig?e=G483WY)

MD5 checksum 91ECD7AAAFFFD4E5A0311B3314C78A21

## Solution
Running `file`:
`DF300-1.001: DOS/MBR boot sector; partition 1 : ID=0xe, start-CHS (0x0,2,4), end-CHS (0x78,254,63), startsector 129, 1950591 sectors, extended partition table (last)`

Opening this in `autopsy` reveals some images which are extracted to `solution/`. Fixing the magic bytes for the file `vol2-C..this-could-be_us.jpg` reveals the flag.

## Flag
`poctf{uwsp_7h3_574r5_my_d3571n4710n}`
