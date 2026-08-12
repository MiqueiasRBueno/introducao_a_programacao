# Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos a seguir para obter o preço de cada produto:
#    Código Preço
#    1      0,50
#    2      1,00
#    3      4,00
#    5      7,00
#    9      8,00
# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

total_comp_pg = qtd_total = 0
cod_produto = {1 : 0.50, 2 : 1, 3 : 4, 5 : 7, 9 : 8}
while True:
    usuario_cod = int(input("Informe o código do produto: "))
    if usuario_cod == 0:
            break
    if usuario_cod in cod_produto:
        qtd_prod_comp = int(input("Informe a quantidade comprada: "))
        qtd_total += qtd_prod_comp
        total_comp_pg += (cod_produto[usuario_cod] * qtd_prod_comp)
    else:
        print("Código inválido!")
print(f"Valor total de sua compra R$ {total_comp_pg:.2f}")
print(f"Foram comprados um total de {qtd_total} de produtos.")
