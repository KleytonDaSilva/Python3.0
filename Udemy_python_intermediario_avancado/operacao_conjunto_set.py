
# Criar conjuntos
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# União de conjuntos
union_set = set1.union(set2)
print(union_set)  # Saída: {1, 2, 3, 4, 5, 6, 7, 8}

# Interseção de conjuntos
intersection_set = set1.intersection(set2)
print(intersection_set)  # Saída: {4, 5}

# Diferença de conjuntos
difference_set = set1.difference(set2)
print(difference_set)  # Saída: {1, 2, 3}

# Diferença simétrica de conjuntos
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Saída: {1, 2, 3, 6, 7, 8}

# Verificar se um conjunto é subconjunto de outro
subset = {1, 2}
is_subset = subset.issubset(set1)
print(is_subset)  # Saída: True

# Verificar se um conjunto é superconjunto de outro
superset = {1, 2, 3, 4, 5, 6}
is_superset = superset.issuperset(set1)
print(is_superset)  # Saída: True

# Verificar se dois conjuntos são disjuntos
disjoint_set = set1.isdisjoint(set2)
print(disjoint_set)  # Saída: False
