from collections import Counter

c = Counter(a=4, b=2, c=3)
c.elements()
print(list(c.elements()))# tra todos os elemenstos 

print(c.most_common()) # tras a quantidade de cada elemento

print(c.most_common(2)) # elementos parecidos em quantidade