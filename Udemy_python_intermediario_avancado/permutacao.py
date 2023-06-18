import itertools

for p in itertools.permutations([1,2,3]): # permutar, trocar os números aleatoriamente
    print(''.join(str(x) for x in p))