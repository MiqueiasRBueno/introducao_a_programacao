# Reescreva o Programa 4.4 e calcule a conta da operadora Tchau usando else.
# Cálculo da mensalidade de um plano de celular da operadora Tchau

plano = str(input("Insira seu plano: "))
preco = minutos_no_plano = extra = 0
if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.2
    preco = 50
if plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preco = 99
if plano == "falopouco" or plano == "falomuito":
    minutos_consumidos = int(input("Insira os minutos consumidos: "))
    print("      Você vai pagar:")
    print(f"Preço do plano: R$ {preco:7.2f}")
    suplemento = 0
    if minutos_consumidos >= minutos_no_plano:
        suplemento = (minutos_consumidos - minutos_no_plano) * extra
        print(f"Minutos extras  R$ {suplemento:7.2f}")
        print(f"Total           R$ {preco + suplemento:7.2f}")
else:
    print("Plano desconhecido!")
