p = 61
q = 53
n = 3233
e = 17
ct = '264,889,119,374,559,357,870,453,4ce,264,77,a5d,87a,170,77,87a,b5a,a5d,119,87a,87a,b5a,2b2,170,96c,70a,77,7aa,870,b5a,6ed,170,5ec'

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
for c in ct.split(','):
    print(chr(pow(int(c, 16), d, n)), end="")
