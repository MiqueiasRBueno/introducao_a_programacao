# Escreva um programa que verifique se um número é palíndromo.
# Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
# Exemplos: 454, 10501

num_palindromo = str(input("Insira um número para verificar se é palíndromo: "))
inicio = 0
final = len(num_palindromo) - 1
while final > inicio and num_palindromo[inicio] == num_palindromo[final]:
    inicio += 1
    final -= 1
if num_palindromo[inicio] == num_palindromo[final]:
    print(f"{num_palindromo} é palíndromo.")
else:
    print(f"{num_palindromo} não é palíndromo.")
