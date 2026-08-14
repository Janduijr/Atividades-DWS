def mostrar(list):
    maior = 0
    menor = 0
    soma = 0
    for x in range(0,len(list)):
        soma += list[x]
        if x == 0:
            maior = list[x]
            menor = list[x]
        else:
            if list[x] > maior:
                maior = list[x]
            elif list[x] < menor:
                menor = list[x]
                
    print(f'o maior valor: {maior}\no menor valor: {menor}\nmedia: {soma/len(list)}')

        
            
    



l = []
for x in range(0,10):
    l.append(int(input(f'digite o {x} numero: ')))
    
mostrar(l)

