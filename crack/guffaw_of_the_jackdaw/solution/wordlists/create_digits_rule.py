import itertools
import string
        
with open("digits.rule", "w") as f:
    chars = [f"${c}" for c in string.digits]

    for i in range(1, 5):
        for comb in itertools.product(chars , repeat=i): 
            rule = " ".join(comb)
            f.write(f"{rule}\n")
