# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos

primeira_lista = []
segunda_lista = []
while True:
    elementos_primeira = int(input('Insira um valor na primeira lista (0 para parar): '))
    if elementos_primeira == 0:
        break
    primeira_lista.append(elementos_primeira)
while True:
    elementos_segunda = int(input('Insira um valor na segunda lista (0 para sair): '))
    if elementos_segunda == 0:
        break
    segunda_lista.append(elementos_segunda)
terceira_lista = []
duas_lista = primeira_lista[:]
duas_lista.extend(segunda_lista)
x = 0
while x < len(duas_lista):
    y = 0
    while y < len(terceira_lista):
        if duas_lista[x] == terceira_lista[y]:
            break
        y += 1
    if y == len(terceira_lista):
        terceira_lista.append(duas_lista[x])
    x += 1
x = 0
while x < len(terceira_lista):
    print(f'{x}: {terceira_lista[x]}')
    x += 1