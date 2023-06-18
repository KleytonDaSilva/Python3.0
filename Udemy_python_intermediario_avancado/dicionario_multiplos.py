from collections import defaultdict

d = defaultdict(list)
d['Kleyton'].append(10) # append são chaves para os dicionairos
d["Marcos"].append(20)
d['Marcos'].append(30)

print(d)

c = defaultdict(set) # dicionarios com set
c['kleyton'].add(20)
c['kleyton'].add(20)
c['kleyton'].add(30)
print(c)