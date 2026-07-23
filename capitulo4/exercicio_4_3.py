# Escreva um programa que leia três números e que imprima o maior e o menor.
num_1 = int(input("Insira o 1° número inteiro: "))
num_2 = int(input("Insira o 2° número inteiro: "))
num_3 = int(input("Insira o 3° número inteiro: "))
maior = num_1
if num_2 > num_1 and num_2 > num_3:
    maior = num_2
if num_3 > num_1 and num_3 > num_2:
    maior = num_3
menor = num_1
if num_2 < num_1 and num_2 < num_3:
    menor = num_2
if num_3 < num_1 and num_3 < num_2:
    menor = num_3
print(f"O maior número é {maior}.")
print(f"O menor número é {menor}.")
