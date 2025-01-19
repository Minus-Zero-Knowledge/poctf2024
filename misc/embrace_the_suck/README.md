# Misc 200-2 - Embrace the Suck 
## Description
💁‍♀️ Lily: so… ignoring me this weekend huh 👀

🧑‍💻 Ben: what? nooo lol. just got this big ctf thing, super hyped for it 😅

💁‍♀️ Lily: right. the *ctf*. didn’t know i was competing w ur hacker obsession 🙄

🧑‍💻 Ben: it’s literally just a weekend. chill. i’ll text u, keep u updated n stuff

💁‍♀️ Lily: “updated” so i get like... play-by-plays? 🥱 “flag captured,” “firewall bypassed”? thrilling.

🧑‍💻 Ben: lmaoo stoppp 😂 ok how bout this: i’ll send u clues. lil secrets

💁‍♀️ Lily: ok now ur talking. spill 👀

🧑‍💻 Ben: alright, first one: *hub 0bbv1 cw hub jr0n*. see if u can crack it 😏

💁‍♀️ Lily: …is that supposed to mean something to me?? 😑 or just some nerd code to keep me quiet while ur off “capturing flags” or whatever

🧑‍💻 Ben: idk maybe it does 😏 or maybe i just know u hate unsolved mysteries

💁‍♀️ Lily: omg. yeah, maybe u just don’t wanna talk to me 😒 mystery solved

🧑‍💻 Ben: c’mon don’t be like that 😅 it’s one weekend. i’ll text u, drop hints, keep u close

💁‍♀️ Lily: u better. bc if all i get is “hub 0bbv1” and zero actual texts, i’m taking my “flag” somewhere else 😈

🧑‍💻 Ben: haha chillll. u know ur the only flag i’m tryna capture ❤️ gimme a lil luck?

💁‍♀️ Lily: whatever. good luck w ur nerd stuff 🖤 just remember who’s actually running the game 👋

## Solution
`hub 0bbv1 cw hub jr0n` looks like a mono-alphabetic substitution of an English phrase. 
(We can use frequency analysis and index of coincidence to support this hypothesis.)

We can probably assume `hub` <-> `the` and `cw` a preposition such as `of` or `in`.
For the remaining 2 words, we have to do some guesswork, but in combination with the title of the challenge, the following seems reasonable:

    0bbv1 <-> needs (4 letter word with 2 e's in the middle)
    jr0n <-> many (4 letter word with n in the 3rd position)

`the needs of the many` is a quote by Spock on Star Trek (https://tvtropes.org/pmwiki/pmwiki.php/Main/TheNeedsOfTheMany) which alludes to the fact that the hero has to make difficult choices.

Finally, we convert the phrase to the flag format.


***Alternative approach***: use https://quipqiup.com/ to automatically solve the ciphertext (but first replace the digits with their respective letter, i.e., "hub obbvi cw hub jron"): 

Using the statistics solver, the top three candidates are:
```
0	-1.273	the needs of the many
1	-1.288	the needs of the king
2	-1.320	the needs of the bank
```


## Flag
`poctf{uwsp_7h3_n33d5_0f_7h3_m4ny}`
