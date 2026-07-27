# Reescreva o Programa 4.4 e calcule a conta da operadora Tchau usando else.
# Cálculo da mensalidade de um plano de celular da operadora Tchau
from capitulo4.programa_4_4 import minutos_consumidos

plano = str(input("Insira seu plano: "))
preco = minutos_no_plano = extra = 0
if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.2
    preco = 50
if plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    plano = 99
if plano == "falopouco" or plano == "falomuito":
    minutos_consumidos = int(input("Insira os minutos consumidos: "))
    print("Você vai pagar:")
    print(f"Preço do plano: R$ {preco:7.2f}")
