def manipula(texto):
    vogais = 0
    inv = texto[::-1]
    pal = False
    for x in texto:
        if x.isalpha():
            if x.lower() in ('a','e','i','o','u'):
                vogais += 1
    
    print(vogais)
    print(inv)
    if texto == inv:
        print('E UM PALINDROMO!')
    else:
        print('NAO E UM PALINDROMO!')
    

texto = str(input('digite um texto: '))
manipula(texto)