# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
#  O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
#  O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

salario = round(float(input("Digite o valor de seu salário: ")), 2)
valor_imovel = round(float(input("Digite o valor do imóvel: ")), 2)
quantidade_de_anos = int(input("Digite em quantos anos deseja pagar: "))
meses = quantidade_de_anos * 12
valor_prestacao_imovel = valor_imovel / meses
valor_sobre_salario = (valor_prestacao_imovel * 100) / salario
if valor_sobre_salario <= 30:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo reprovado!")
