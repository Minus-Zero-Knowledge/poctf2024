# Crack 200-2 - Undocumented Outrage
## Description
There's a lot to like about where I live. There's beautiful wilderness. You're never more than thirty feet from a tavern, bank, and fast food restaurant. And thanks to the university there are some unique opportunities. When I was in high school I started learning Russian. My choices were French, German, Spanish, or Russian. Most school districts in the USA only offer the first three, if they have any foreign language programs at all. I picked Russian because I thought it would be the hardest and I am a total fool. But I stuck with it. I was determined to learn and Госпожа Демовидова was determined to teach me. I ended up taking it longer than I technically had to. Two years in high school and four years in university.

Anyway, there's plenty to dislike about where I live, too. Like the cold. I realize that many of you might be from cold climates, but I'm taking cold. As in below zero for many weeks most years. So cold that if you throw a cup of water in the air it will be frozen solid by the time it hits the ground. So cold that if you take some rolls right out of the oven they'll be delicious and hot. Set them near an open window to cool and they will be cold in seconds. And no one likes cold rolls. Cold rolls steal all the joy warm bread brings.

I suppose I'm rambling enough. We should probably get to the challenge. Here's an encrypted doc file. I seem to have forgotten the password, but I'm sure you'll find it as long as you can stay cool under pressure.

Right Click, Save As... [Пока железо холодное, куй](https://pointeroverflowctf.com/static/Crack200-2.docx)

MD5 checksum 4AAC3FAF34C758C5B4351D187F0475E3

## Solution
The given file is an MS Office Word 2013 password-protected file. Extract the hash and perform a dictionary attack using `hashcat` or `john`.

The main challenge was to find a good dictionary of Russian words. Using wordlists containing common Russian words (such as https://github.com/hingston/russian) did not yield results. 
Ultimately, the right dataset was found from https://ruscorpora.ru/en.

Password is **холоднокатаного**.

```
$ wget https://ruscorpora.ru/new/ngrams/1grams-3.zip
$ unzip 1grams-3.zip
$ grep холоднокатаного 1grams-3.txt 
> 18	холоднокатаного
```

"холоднокатаного" translated to English is [cold-rolled](https://www.deepl.com/en/translator#ru/en-us/%D1%85%D0%BE%D0%BB%D0%BE%D0%B4%D0%BD%D0%BE%D0%BA%D0%B0%D1%82%D0%B0%D0%BD%D0%BE%D0%B3%D0%BE).

## Flag
`poctf{uwsp_wh15p3r5_1n_7h3_d4rk}`
