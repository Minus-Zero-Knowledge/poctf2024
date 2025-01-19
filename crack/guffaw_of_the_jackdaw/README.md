# Crack 300-1 - Guffaw of a Jackdaw
## Description
Boy, these Crack challenges... You know, I seriously considered not including them this year. They're so dull. Like watching paint dry. I spent a lot of time trying to think of way to make them interesting. You know the worst part is that they don't really teach very practical skills? Social engineering is more reliable, and a little recon is usually better for building tailored dictionaries. Just look at the most common password lists - sports, cartoons that were popular when they were kids, food, sex, family members, pets, birthdays, all regularly appear as popular choices. Things we know, things we like. In fact, let's put it to the test...

Here's Jack. He loves monster trucks. Like, REALLY likes them.

He loves them so much, his monster truck is his daily driver.

Every chance he gets, he goes out to jams and exhibitions.

Jack is a man that like BIG things only. Sliders? No, Jack likes the burger that weighs a full kilo. Petite fours? Jack says he's a grand fours man. Little Italy? Get out of here with that. Jack will have a worldwide Italian empire or nothing at all!

Jack recently asked me for advice. He's required to change his password every year at work. Well, he forgot it! He wanted to know if he should use a password vault to avoid this in the future since he tends to just add numbers to the end of his password and increment them each time they need to be changed. The answer is certainly yes, but I bet you can figure out his password just based on this information alone. If you figure it out, use it on this file. I'm sure you recognize this icon, so I don't need to tell you what to do with it.

![Crack300-1.png](public/Crack300-1.png)

MD5 checksum D97BDBF47999D3D78E9BF317244D663A


## Solution
Using [Bing image reverse search on the image](https://www.bing.com/images/search?view=detailV2&insightstoken=bcid_qFDMIAT5.p4Hug*ccid_UMwgBPn%2B&form=SBIWEB&iss=SBIUPLOADGET&sbisrc=ImgDropper&idpbck=1&sbifsz=36+x+36+%c2%b7+1.20+kB+%c2%b7+png&sbifnm=Crack300-1.png&thw=36&thh=36&ptime=23&dlen=1644&expw=36&exph=36&selectedindex=0&id=-108531554&ccid=UMwgBPn%2B&vt=2&sim=11) we learn that this is the icon of the program OpenStego (https://www.openstego.com/). This means that the flag is hidden in the image (and encrypted with a password).

Workflow: assemble dictionary with words relating to monster trucks, in the format {MONSTERTRUCK}{Number}, and try decrypting via the command line tools of OpenStego (https://www.openstego.com/cmdline). Additionally, the text hints that the password should be all caps.

The password is found to be **MONSTERJAM24**.

## Flag
`poctf{uwsp_p4r7_0f_7h3_m4ch1n3}`
