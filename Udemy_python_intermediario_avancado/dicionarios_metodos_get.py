
d = {'marcos':28, 'Kleyton':36, 'maria':25}
print(d)

print(d.get('Kleyton'))

if d.get('blabla'):
    print('chave existente')
else:
    print('chave inexistente')
    