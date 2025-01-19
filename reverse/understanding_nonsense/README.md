# Reverse 100-3 - Understanding Nonsense
## Description
Oh, boy... Only Wave 2 and I'm already exhausted. Whatever the issue, I just can't be bothered to finish putting this challenge together. Here, this what I have so far. Started working on the decode function and gave up. You go ahead and do the rest and the flag is yours! And if Prof. Johnson asks, tell him this was really well done or I'll get in trouble.

Right Click, Save As... [Reverse100-3](https://pointeroverflowctf.com/static/Reverse100-3)

Right Click, Save As... [Reverse100-3 Source Code](https://pointeroverflowctf.com/static/Reverse100-3.c)

## Solution
Completing the reverse source code:
```c
// Reverse the modifications 10 times
for (int step = 1; step <= 10; step++) {
    reverse_modify_flag(encoded_flag, seed);
    //print_flag_hex(encoded_flag, length, step);
}

printf("Decoded flag (plaintext in hex): ");
print_flag_hex(encoded_flag, length, 10);  // Print final decoded flag in hex
```

When running the resulting program: `Decoded flag (plaintext in hex): 706f6374667b757773705f627233763137795f31355f3768335f353075317d`

Decoding the plaintext in hex: `echo -n 706f6374667b757773705f627233763137795f31355f3768335f353075317d | xxd -r -p`

## Flag
`poctf{uwsp_br3v17y_15_7h3_50u1}`
