# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do
# aumento. Exiba o valor do aumento e do novo salário.
salario_atual = round(float(input("Qual o salário atual?: ")), 2)
porc_aumento = round(float(input("Quanto aumentar?: ")), 2)
aum_salario = (salario_atual * porc_aumento) / 100
nv_salario = (aum_salario + salario_atual)
print(f'''Valor do aumento concedido: R$ {aum_salario:.2f}
Novo valor do salário: R$ {nv_salario:.2f}''')
