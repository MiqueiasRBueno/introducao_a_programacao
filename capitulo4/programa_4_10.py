# Programa 4.10: Planos da Tchau com elif
valido = True
plano = str(input("Qual é seu plano de celular?: "))
if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.2
    preco = 50
elif plano == "falomuito":
    minutos_no_plano = 500
    extra =  0.15
    preco = 99
else:
    valido = False
if not valido:
    print(f"Erro: Não conheço este plano {plano}")
else:
    minutos_consumidos = int(input("Quantos minutos você usou esse mês?: "))
    print("Você vai pagar:")
    print(f"Preço do plano: R$ {preco:10.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f'Suplemento:     R$ {suplemento:10.2f}')
    print(f"Total:          R$ {preco + suplemento:10.2f}")
