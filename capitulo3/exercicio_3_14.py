# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a
# quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km_percorrido = round(float(input("Insira a quilometragem rodada: ")),2)
dias_locados = int(input("Insira a quantidade de dias locado: "))
valor_dias = dias_locados * 60
valor_km = 0.15 * km_percorrido
total_pg = valor_km + valor_dias
print("Total a pagar pelo veículo: R$%5.2f" %total_pg)
