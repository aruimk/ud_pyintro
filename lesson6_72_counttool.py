

s = 'fajl;dfkjasl;fdkas;ldkfja;lkjf'

d = {}

for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print('d')
print(d)



e = {}
for c in s:
    e.setdefault(c,0)
    e[c] += 1
print('e')
print(e)


from collections import defaultdict
f = defaultdict(int)
for c in s:
    f[c] += 1
print('f')
print(f)

