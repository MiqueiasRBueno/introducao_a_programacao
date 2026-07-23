# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#  Para os inferiores ou iguais, de 15%.

salario = float(input("Insira o valor de seu salário: "))
base = salario
if base > 1250:
    novo_salario = base + (base * 0.1)
if base <= 1250:
    novo_salario = base + (base * 0.15)
print(f"Novo salário R${novo_salario:6.2f}")
