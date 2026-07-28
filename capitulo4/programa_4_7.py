# Conta de telefone com três faixas de preço

minutos_usados_mes = int(input("Quantos minutos você utilizou esse mês?: "))
preco = 0
if minutos_usados_mes < 200:
    preco = 0.2
else:
    if minutos_usados_mes < 400:
        preco = 0.18
    else:
        preco = 0.15
print(f"Você vai pagar este mês: R$ {minutos_usados_mes * preco:6.2f}")
