# DF 400 - No Irony in Rain
## Description
I know this is probably not a good use of the contest, but I figure I have a lot of brainpower between the lot of you and I could use the help. Here's the situation: I had a really cool idea. I was going to finance an independent film called, "POCTF 2024: The Movie." A big-budget, sci-fi, action, rom-com starring Yours Truly. Worldwide distribution with premiere releases in New York, Moscow, Toronto, Dubai, Karnataka, and it was going to be THE movie event of this century. I got a screener copy right before the start of the contest. I decided to post it to YouTube to get some comments. You know, like a test screening. Things were going great. I had 24 veiws after just one week of having it up on my channel. Then it really started blowing up. It went viral, and I had 506 veiws at the end of the weekend! A smash hit! But then I started getting weird comments on the video. People posting "xaxaxaxaxa" and ")))" a lot. I don't know what that means, but I naturally assumed it was some kind of attack. I need you to comb through the video and tell me if anything seems fishy to you. Here's an exact copy of the video that I uploaded to my channel for you to review.

Right Click, Save As... [Straight to Streaming Release](https://pointeroverflowctf.com/static/DF400.mov)

MD5 checksum F9F59E003B96F2A6C8521FB8B2A29BB1

## Solution
The text references the upload to this YouTube channel: https://www.youtube.com/@AFascinatingChap. More specifically, the video is located at https://www.youtube.com/watch?v=7lDXor8OryQ

At first glance, everything looks completely the same as the provided attached version.

However, in the description, there is a link to follow along with the transcript for the video. This shows "something fishy"
```
0:30 [red herring] 
      /"*._       _ 
  .-*'` `*-.._.-'  /
<*))               ( 
  `*-._`._(__.--*"`.\ 
```

Change the language to Russian, now use Google Translate to translate the complete text; or just jump straight to the 0:30 timestamp where 
the following is mentioned:
```
JTSUKEN -> QWERTY
0:30
зщсеаХгцыз_50_17_6035Ъ
```

This references the JCUKEN keyboard mapping: https://en.wikipedia.org/wiki/JCUKEN

Use the JCUKEN to QWERTY keyboard mapping as shown here: https://upload.wikimedia.org/wikipedia/commons/a/a4/ES1845_keyboard.jpg to decode the secret message.

## Flag
`POCTF{UWSP_50_17_6035}`

