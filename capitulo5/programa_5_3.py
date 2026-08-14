# Tabuada sem repetições aninhadas

tabuada = numero = 1
while tabuada <= 10:
    print(f"{tabuada} X {numero} = {tabuada * numero}")
    numero += 1
    if numero == 11:
        print()
        numero = 1
        tabuada += 1
