# DF 200-3 - Never Met the Pieman
## Description
The title of this challenge isn't a clue. It's a complaint. I took the family on vacation last summer. Can't remember where. Some city in Europe or Italy or Zealand or something. The wife wanted to go to some museum where they had some statue called the Pieman. Flew all the way there and stood in line all day. I ask the wife when we're going to see the Pieman, and she gives me this look like I'm speaking alien. No idea what I'm talking about. Whatever, by this point I'm so bored and the wife is telling me to record some of this stuff so we have memories for later. I pull out my camera and shoot this video. Decided to spruce it up a little with my awesome video editing skills. I guess none of this really matters for the purposes of this challenge, but feel free to check it out for yourself.

Right Click, Save As... [Is the Pieman a Cryptid](https://pointeroverflowctf.com/static/DF200-3.mov)?

## Solution
The name of Track2 is the base64 encoded flag.
```
$ exiftool DF200-3.mov
Track 2 Name                    : cG9jdGZ7dXdzcF83MW0zXzNuMHVnaF9mMHJfbDB2M30=
```

## Flag
`poctf{uwsp_71m3_3n0ugh_f0r_l0v3}`
