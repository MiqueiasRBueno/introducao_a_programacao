# Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo,
#  assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado.
#  Lembre-se de que podemos entender o quociente da divisão de
#  dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. 
# Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

dividendo = int(input("Insira o número que deseja dividir: "))
divisor = int(input("Insira o número divisor: "))
x = 0
if dividendo > divisor:
    while dividendo >= divisor:
        dividendo -= divisor
        x += 1
        resto_da_divisao = dividendo
    print(f"{dividendo} / {divisor} = {x} Resto da divisão {resto_da_divisao}")
else:
    print("Divisão inválida!")
