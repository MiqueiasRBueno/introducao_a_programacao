# Escreva um programa que leia um número e verifique se ele é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos
# os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero,
# o número não é primo. Observe que 0 e 1 não são primos e que 2 é o únoco número par que é primo.

# Solicita um número inteiro ao usuário e o armazena na variável 'n'
num_verificar_primo = int(input("Insira um número inteiro para verificar se é primo: "))
if num_verificar_primo <= 1:
    print(f"{num_verificar_primo} não é primo.")
else:
    primo = True
    dividendo = num_verificar_primo
    divisor = 2
    while divisor < dividendo:
        if dividendo % divisor == 0:
            primo = False
        divisor += 1
    if primo == False:
        print(f"{num_verificar_primo} não é primo.")
    else:
        print(f"{num_verificar_primo} é primo.")
