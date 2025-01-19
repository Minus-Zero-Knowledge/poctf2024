# Crack 100-2 - I Have Written Down My Secrets
## Description
Summer breaks are great, but I can't stand the downtime. I need to keep my mind occupied. I need a project, a puzzle, a challenge. It's not about staying productive, per se. I just need to keep this mind moving or I'll get bored. I've found the hobby that is presently perfect without being too invested: Learning languages. Simple, no-pressure, infinitely valuable, and a great intellectual challenge. This summer I went a little overboard and overindulged in Duo's offerings. I spent at least a few hours every day learning Spanish, French, German, Italian, Russian, Mandarin, Arabic, Finnish, Hindi and Swedish. I know, that's obviously way too many languages to attempt at once, but it's easy to over-commit and spread myself thin when there are so many wonderful options available. French was actually my focus this summer. I had so much fun learning that I would over-zealously do extra lessons. Is Duo the best way to learn? Non! Am I really learning all that much in the end? Occupez-vous de vos oignons! After a summer of learning am I able to even communicate at all in French? Absolument pas! Je te dis, c'était mieux que de mater les JO à Paris cet été.

Clic droit, Enregistrer sous... [Crack100-2.pdf](https://pointeroverflowctf.com/static/Crack100-2.pdf)

MD5 checksum: 978A017C772FAA17A0DBFC25561A499D

## Solution
Perform a dictionary attack (using French words) using e.g. `hashcat` (or `pdfcrack`).

We used https://github.com/clem9669/wordlists/blob/master/dictionnaire_fr as dictionary.
Simply using this as a wordlist did not give the correct password; we had to apply additional rules from `best64.rule` to the `hashcat` rule engine.

The password is ultimately found to be **surinvesti**. The wordlist we used only had `surinvestir`, as an infinitive, but one of the rules also produced candidates with the last character removed.

The decrypted pdf reveals a base64 encoded string of the flag: `cG9jdGZ7dXdzcF9XMW5kNV8wZl9DaDRuZzN9`.

There is a hint in the description regarding the password (which was found only retrospectively): 
> I've found the hobby that is **presently perfect without being too invested**

## Flag
`poctf{uwsp_W1nd5_0f_Ch4ng3}`
