# Escreva um programa que leia um número e verifique se ele é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos
# os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero,
# o número não é primo. Observe que 0 e 1 não são primos e que 2 é o únoco número par que é primo.

num_primo = int(input("Insira um número "))
num = num_primo
if num <=1:
    primo = False
else:
    primo = True
    limite = int(num ** 0.5)
    for v in range(2, limite + 1):
        if num % v == 0:
            primo = False
            break
if primo:
    print(f"{num_primo} é primo.")
else:
    print(f"{num_primo} não é primo.")
