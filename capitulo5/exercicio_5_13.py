# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
# Pergunte também o valor mensal que será pago.
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

valor_divida = float(input("Insira o valor de sua dívida: "))
juros_mes = float(input("Insira a taxa de juros cobrada: ")) / 100
pag_mensal = float(input("Insira o valor pago mensalmente: "))
saldo = valor_divida
juros = amortizacao = juros_pago = 0
mes = 1
while saldo > pag_mensal:
    juros = saldo * juros_mes
    amortizacao = pag_mensal - juros
    saldo -= amortizacao
    juros_pago += juros
    mes += 1
    print(f"O saldo da dívida do mês {mes} é de {saldo:.2f}")
print(f"Prazo necessário para quitar a dívida de R$ {valor_divida:.2f} a uma taxa de {juros_mes}%")
print(f"é de {mes - 1} meses. Pagando um total de R$ {juros_pago:.2f} de juros.")
print(f"No último mês teria um saldo residual de R$ {saldo:.2f} à pagar.")
