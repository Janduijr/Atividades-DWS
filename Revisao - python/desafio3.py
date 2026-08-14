def compressao(lista):
    dic = {}
    for item in lista:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    print(dic)
    

lista = ["Ana", "Bruno", "Carlos", "Ana", "Bruno", "Ana",'jandui', 'jandui']
compressao(lista)