# Web 300-2 - Emperfect Copies 
## Description
Welcome - to Star Talent Agency! I'm telling you, kid, you've got "it." You know, that little something something. The pizazz. The razzmatazz. Kid, you've got that Jinny Way Tois. That's French, kid, keep up. It means you're going places and I can take you there. I'm an agent, you see? Know what that means? Don't worry about it. In fact, you won't have to worry about a THING ever again. All you gotta do is show up on set and look good for the camera. No more 9 to 5. No more looking for hidden login pages and restricted admin/flag routes. You've got it made!

All I need you to do for me - head to this site and upload your head shot to the agency database so casting agents can see that beautiful mug of yours. Keep it safe for work, though. We don't manage that kind of talent. I've got it restricted to only accept png and jpg files, so no funny business. Also, fame is fleeting in Hollywood, so I'm afraid you've only got 60 seconds from the time of your upload to make it big before your head shot gets taken off the site and you're going straight-to-video.

Your target: [Goin' Out West Where The Wind Blows Tall](http://34.135.223.176:5250/)

## Solution
There is a POST `/login` endpoint on the site. Guess the admin JWT token with username `admin` and password `admin123`.
Make GET request to `/admin/flag` endpoint [with this token](https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token).

## Flag
`poctf{uwsp_kn0wl3dg3_1753lf_15_p0w3r}`
