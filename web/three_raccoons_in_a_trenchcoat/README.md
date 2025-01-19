# Web 200-3 - Three Racoons in a Trenchcoat
## Description
When designing the contest, I sometimes like to use themes. The theme for the Web challenges, you may have realized by now, is that the websites are never exactly what the challenge text tells you they will be. I go on about how the site will be one thing, then you click and it's some humorous alternative.

Well, not this time. This time, I'm going to give you a challenge that is exactly what the challenge text says it will be.

It is probably not significant that I have chosen just this one challenge to be completely honest.

Do make sure you are familiar with the [hints](https://pointeroverflowctf.com/Hints) for Web challenges before you begin work on this one. I'd hate to see someone forced to sit out of the Web challenges for the remainder of the contest. Especially when the contest is designed to release all the high value challenges after this one. Not sure why I'd do that, but it's probably best to make like three raccoons in a trench coat, try to blend in and not draw too much attention to yourself.

[Once upon a time...](http://34.135.223.176:24100/storybook?page=1)

## Solution
Run `gobuster` to enumerate hidden pages by fuzzing the `page` parameter. 

The page containing the flag is under **archive**: `http://34.135.223.176:24100/storybook?page=archive`

## Flag
`poctf{uwsp_h3ll_15_07h3r_p30pl3}`
