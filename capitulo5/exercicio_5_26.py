# Escreva um programa que calcule o resto da divisão inteira entre dois números.
# Utilize apenas as operações de soma e subtração para calcular o resultado.

# Solicita ao usuário o número que será dividido e o converte para inteiro
num_dividendo = int(input("Insira um número para o dividendo: "))

# Solicita ao usuário o número pelo qual se vai dividir e o converte para inteiro
num_divisor = int(input("Insira um número para o divisor: "))

# Inicializa a variável do resto com o valor total do dividendo
resto_divisao = num_dividendo

# Cria um laço que repete enquanto o valor restante for grande o suficiente para ser subtraído pelo divisor
while resto_divisao >= num_divisor:
    # Subtrai o divisor do valor restante (subtração sucessiva)
    resto_divisao -= num_divisor

# Exibe na tela o resultado, mostrando o resto que sobrou após todas as subtrações
print(f"O resultado da divisão inteira entre {num_dividendo} % {num_divisor} = {resto_divisao}.")
