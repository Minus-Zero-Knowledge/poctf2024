s = "optc{fwups1_4__mh7_3c043}n"
it = iter(s)
print("".join(f"{y}{x}" for x,y in zip(it, it)))
