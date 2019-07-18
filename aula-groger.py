import random
lista = []
numeros = 0

while numeros < 30:
    lista.append(random.randrange(1,200))
    numeros +=1
# def maior_numero(lista):
#     valormax = lista[0]
#     for numeros in lista:
#       if numeros>valormax:
#           valormax = numeros
    # return valormax

def maior_numero(lista):
    return max(lista, key=int)

print(f'Maior valor:{maior_numero(lista)}')

print (f'ESSA È SUA : {lista}')

