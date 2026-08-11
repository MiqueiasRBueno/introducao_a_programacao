# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

valor_deposito_inicial = float(input("Insira o valor do seu depósito: "))
investimento_mensal = float(input("Insira o valor de seu investimento mensal: "))
taxa_juros = float(input("Insira o valor da taxa de juros: ")) / 100
mes = 1
saldo = valor_deposito_inicial
while mes <= 24:
    saldo += (saldo * taxa_juros) + investimento_mensal
    print(f"Saldo do mês {mes} é de R$ {saldo:5.2f}")
    mes += 1
print(f"O lucro acumulado é de R$ {saldo - valor_deposito_inicial:8.2f}")
