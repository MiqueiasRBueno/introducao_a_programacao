# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada,
# em vez de começar com 1 e 10.

n = int(input("Tabuada de: "))
inicio_tabuada = int(input("Digite o número de início da tabuada: "))
fim_tabuada = int(input("Digite o número do final da tabuada: "))
while inicio_tabuada <= fim_tabuada:
    print(f"{n} x {inicio_tabuada} = {n * inicio_tabuada}")
    inicio_tabuada += 1
