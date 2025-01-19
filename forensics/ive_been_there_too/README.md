# DF 100-3 - I've Been There Too    
## Description
Attached to this challenge is a sqlite file. It's a simulated student database where someone has come in afterward to make a few modifications. In my entire career, I've never had a student break into the student information system to change their grade or add credits they didn't earn, but it's always something I've thought about. I see it as a classic paradox of risk analysis and game theory. But this isn't the place for that discussion. Enjoy the challenge!

Right Click, Save As... [DF100-3.sqlite](https://pointeroverflowctf.com/static/DF100-3.sqlite)

MD5 checksum 9F21964B6CAA96DE843E4C9B872B16F0

## Solution
Run `strings` and `grep`:
 - `poctf` -> `poctf{`
 - `uwsp` -> `uwsp_d0_4ndr01d5` 
 - `}` -> `_dr34m}`

Alternatively, use a SQLite Database browser and search in the `name` column for these strings.

## Flag
`poctf{uwsp_d0_4ndr01d5_dr34m}`