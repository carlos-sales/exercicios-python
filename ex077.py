palavras = ('Laptop',
            'Mouse',
            'Celular',
            'Mochila',
            'Melatonina')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
