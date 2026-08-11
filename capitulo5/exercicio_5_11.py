# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

valor_deposito_inicial = float(input("Insira o valor á depositar na poupança: "))
taxa_juros = float(input("Insira o valor da taxa de juros da poupança: ")) / 100
mes = 1
saldo = valor_deposito_inicial
while mes <= 24:
    saldo += (saldo * taxa_juros)
    print(f"O saldo do mes {mes} é de {saldo:5.2f}")
    mes += 1
print(f"O lucro obtido é de R$ {saldo - valor_deposito_inicial:5.2f}")
