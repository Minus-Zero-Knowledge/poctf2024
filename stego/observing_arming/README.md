# Stego 300-1 - Observing Arming
## Description
You might have heard that I had aspirations of making a movie about the contest. Well, we've managed to create a trailer for it, but it hasn't been going very well. It's hard work! Watching the budget, hiring a competent crew, dealing with writers that all think they're the modern Mark Twain. It's ridiculous. But the worst part - dealing with those actors. They all think they're the center of the universe. They're not. It's not about them... ... ...

It's about me! I deserve the best lines. I should be on camera about 90% of the movie and there better be a plate of Cheese Nips arranged in four neat little rows with a glass of 8.6oz of 14C water waiting for me at the craft services table, because that is in my contract! You know what? I can't work under these conditions! I'll be in my trailer...

Right Click, Save As... [Aliens Riding Horseback Picking Carrots](https://pointeroverflowctf.com/static/Stego300-1.mkv)

MD5 checksum CF9D0A7CE079101A909CE06A6FD653EE

## Solution
Using `mkvinfo`, notice that there is a track with identifier 2 which is not audible in the video. This track can for example be extracted with `mkvextract Stego300-1.mkv tracks 1:track1` or `ffmpeg -i Stego300-1.mkv -map 0:a:1 -c copy output.wav`. Opening this audio file in `audacity` shows rectangular waves. The signal seems to loop every 2 seconds. Computing a run-length encoding of the highs and lows shows that the contiguous lengths occur in groups. Each such length corresponds to a character of the flag. See `solution/solution.txt` for each group length and the corresponding character.

## Flag
`poctf{uwsp_31em3n74ry_my_d34r_w4750n}`