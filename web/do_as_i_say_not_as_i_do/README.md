# Web 300-1 - Do As I Say Not As I Do
## Description
Can't believe we're almost done... I bet by now you're asking: "Gee, Professor J, you must be some kind of mega-genius. How do you come up with all these ideas?" Well, I have a little secret sauce. Music.

That's right. Performance-enhancing tunes. I play them in the morning to get pumped up. I play it while I'm coming up with challenges. I play it while I cry in the shower. I play it while I'm trying to sleep but can't because the music is too loud.

I even have a favorite streaming platform. It's not that well known, but I like it because you can make playlists and share them out with direct links. Unfortunately, this summer as I was prepping the contest I was rocking out to some tunes when I noticed a little bug on their site. A vulnerability in their upload form. I let them know, of course, and it looks like they've handled it. Good thing, too, because I happen to know they keep some very interesting information in an environment variable on the back end.

Your target is [EVERY MORNING I WAKE UP AND OPEN PALM SLAM MY MOUSE TO CLICK THE PLAY BUTTON
](http://34.135.223.176:10405/)

## Solution
First gain user credentials via some fuzzing: `("username" : "TheProfezzorJ", "password": "password")`
After login, there is an `/upload` endpoint which is disabled on the site (client-side), but still available on the server as a POST request.
Perform SSTI on this endpoint in the description parameter, which is evaluated and sent back. This can be easily verified by sending `{{ 7*7 }}`.

The environment variables can be read by using following payload:
```
{{ config.__class__.__init__.__globals__['os'].popen('env').read() }}
```

## Flag
`poctf{uwsp_70_7h1n3_0wn_53lf_b3_7ru3}`
