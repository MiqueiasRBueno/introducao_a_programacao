# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

valor_prod = round(float(input("Insira o valor do produto: R$ ")), 2)
perc_desc = int(input("Insira a porcentagem a descontar: "))
valor_desc = valor_prod * perc_desc / 100
total_pg = valor_prod - valor_desc
print(f'''Total do desconto: R${valor_desc:.2f}
Total à pagar: R${total_pg:.2f}''')
