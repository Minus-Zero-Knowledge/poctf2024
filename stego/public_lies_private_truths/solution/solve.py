with open('../public/encode_grid.js', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

import re
filters = []
opacities = []

for l in lines:
    filter_pat = r'brightness\((\d+)%\)'
    if m := re.search(filter_pat, l):
        filters.append(m.group(1))
    
    opacity_pat = r'opacity = (.*);'
    if m := re.search(opacity_pat, l):
        opacities.append(m.group(1))

assert len(filters) == len(opacities)
print(filters)
mp = {}
import string

lower = string.ascii_lowercase
subst = ''
for i in range(len(filters)):
    curr = (filters[i], opacities[i])
    if curr in mp:
        subst += mp[curr]
    else:
        mp[curr] = lower[len(mp)]
        subst += mp[curr]

print(subst)
# abcdefghiajklmjenocmjhpqqjrmjhpkljsngt
# poctf{uwsp_
# klm enocm hpqq rm hpkl sng
# the force will be with you