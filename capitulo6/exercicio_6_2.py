# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras

primeira_lista = []
segunda_lista = []
while True:
    elementos_primeira = int(input("Insira um valor para primeira lista (0 para parar): "))
    if elementos_primeira == 0:
        break
    primeira_lista.append(elementos_primeira)
while True:
    elementos_segunda = int(input("Insira um valor para segunda lista (0 para parar): "))
    if elementos_segunda == 0:
        break
    segunda_lista.append(elementos_segunda)
terceira_lista = primeira_lista[:]
terceira_lista.extend(segunda_lista)
parada = 0
while parada < len(terceira_lista):
    print(f'{parada + 1}: {terceira_lista[parada]}')
    parada += 1
