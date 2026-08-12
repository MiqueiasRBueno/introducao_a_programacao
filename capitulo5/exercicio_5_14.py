# Escreva um programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

qtd_num_dig = soma = 0
while True:
    insira_num = int(input(f"Insira o {qtd_num_dig + 1}° número: "))
    if insira_num == 0:
        break
    soma += insira_num
    qtd_num_dig += 1
media = soma / qtd_num_dig
print(f"Foram digitados {qtd_num_dig} números.")
print(f"O valor da soma entre os números digitados é de {soma}")
print(f"A média entre os números digitados é de {media:.2f}")
