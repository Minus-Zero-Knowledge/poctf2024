# OSINT 200-1 - Something to Say About It
## Description
I have a dynamite idea! Let's go on a little snake hunt. Now, where do you find snakes? That's right, in snake pits! How do you find snake pits? By following the clearly marked signs to the designated snake dumping pit locations, of course! Surely you've seen those around your city, right? They probably look a little like this one:



I'll even give you a little help by zooming out a little. You're not xanthophobic, are you?



You know, while we're here, I'm going to grab a fresh password for the archive that contains the flag. As a memento to remember our hunting expedition. The phone number on the sign back there should do. Numbers only, no parenthesis, no spaces, no dashes.



Right Click, Save As... [There's a Snake In My Boot](https://pointeroverflowctf.com/static/OSINT200-1_flag.zip)

MD5 checksum B0752B12B005DC132CA4BA2C90F06629

## Solution
Search around via [Bing reverse image search using the sign of "Snake Pit"](https://www.bing.com/images/search?q=imgurl:https%3a%2f%2ftemp-ca.s3.amazonaws.com%2fcdn-files%2f218271728843144.jpg%3fX-Amz-Content-Sha256%3dUNSIGNED-PAYLOAD%26X-Amz-Algorithm%3dAWS4-HMAC-SHA256%26X-Amz-Credential%3dAKIA2YDWKLAVUAFT3HFY%252F20241013%252Fus-east-1%252Fs3%252Faws4_request%26X-Amz-Date%3d20241013T181224Z%26X-Amz-SignedHeaders%3dhost%26X-Amz-Expires%3d1200%26X-Amz-Signature%3d5172d387e128f5a2204287d0ee15fc79bcbb5866d464c74aec619450a4df7ab3&view=detailv2&selectedindex=0&iss=VSI&form=IRSBIQ&id=24E0BE226C5FC495EDEE6FEE2FAAEE604D571E49&ccid=i4IzK9sf&mediaurl=https%3A%2F%2Fcdn.acidcow.com%2Fpics%2F20120713%2Fstanley_marsh_around_amarillo_54.jpg&exph=525&expw=700&vt=2&sim=15&simid=607993028696890694&ck=076758B439362BBDD62BD7603435B748&thid=OIP.i4IzK9sf4xNo7xAfYViQiQHaFj&cdnurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.8b82332bdb1fe31368ef101f61589089%3Frik%3DSR5XTWDuqi%252fubw%26pid%3DImgRaw%26r%3D0&pivotparams=imgurl%3Dhttps%253A%252F%252Ftemp-ca.s3.amazonaws.com%252Fcdn-files%252F218271728843144.jpg%253FX-Amz-Content-Sha256%253DUNSIGNED-PAYLOAD%2526X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIA2YDWKLAVUAFT3HFY%25252F20241013%25252Fus-east-1%25252Fs3%25252Faws4_request%2526X-Amz-Date%253D20241013T181224Z%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Expires%253D1200%2526X-Amz-Signature%253D5172d387e128f5a2204287d0ee15fc79bcbb5866d464c74aec619450a4df7ab3).

This leads us to [this site](https://izismile.com/2012/07/14/unconventional_art_signs_66_pics.html) which mentions the artist name and backstory of the sign.
> Stanley Marsh, an artist from Amarillo, Texas is known for erecting signs that look like public signs but have very unusual messages.

You can also read more [here](https://www.reddit.com/r/pics/comments/we9rl/stanley_marsh_an_eccentric_millionaire_in_my/).

After searching on Google maps for Amarillo and NW 3rd avenue, we find the location of the photos, i.e. [2811 NW 3rd Ave, Amarillo, TX 79106, USA](https://maps.app.goo.gl/gBXGuhwa77aMQKon6).

The sign contains the phone number: 806-340-7320. 
Open the zip file with the password **8063407320**.


## Flag
`poctf{uwsp_f07r7un3_f4v0r5_7h3_b01d}`
