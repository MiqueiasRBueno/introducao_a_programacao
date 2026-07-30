# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
#  Pergunte a quantidade de kWh consumida e o 
# tipo de instalação: R para residências, I para indústrias e C para comércios. 
# Calcule o preço a pagar de acordo com a tabela a seguir.
# +---------------------------------------+
# |   Preço por tipo e faixa de consumo   |
# +---------------------------------------+
# | Tipo        | Faixa (kWh)   | Preço   |
# +=======================================+
# | Residencial | Até 500       | R$ 0,40 |
# |             | Acima de 500  | R$ 0,65 |
# +---------------------------------------+
# | Comercial   | Até 1000      | R$ 0,55 |
# |             | Acima de 1000 | R$ 0,60 |
# +---------------------------------------+
# | Industrial  | Até 5000      | R$ 0,55 |
# |             | Acima de 5000 | R$ 0,60 |
# +---------------------------------------+

energia_consumida = int(input("Insira quantos kwh foram consumidos: "))
tipo_de_instalacao = str(input("""Insira o tipo de instalação: 
R - Residencial
C - Comercial
I - Industrial
Tipo de instalação: """)).title()
if tipo_de_instalacao == "R":
    if energia_consumida < 500: preco = 0.4
    else: preco = 0.65
elif tipo_de_instalacao == "C":
    if energia_consumida < 1000: preco = 0.55
    else: preco = 0.6
elif tipo_de_instalacao == "I":
    if energia_consumida < 5000: preco = 0.55
    else: preco = 0.6
print(f"Total a pagar:   R$ {energia_consumida * preco:6.2f}")
