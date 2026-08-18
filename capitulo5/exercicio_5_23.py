# Escreva um programa que leia um número e verifique se ele é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos
# os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero,
# o número não é primo. Observe que 0 e 1 não são primos e que 2 é o únoco número par que é primo.

# Solicita um número inteiro ao usuário e o armazena na variável 'n'
n = int(input("Insira um número para verificação de números primos: "))

# Cria uma cópia do valor de 'n' na variável 'primo' (usada no restante do cálculo)
primo = n

# Calcula a raiz quadrada do número e converte para inteiro.
# Propriedade matemática: se um número tem um divisor, pelo menos um deles é menor ou igual à sua raiz quadrada.
# Isso reduz drasticamente a quantidade de repetições (iterações) que o programa precisa fazer.
raiz_primo = int(primo ** 0.5)

# Inicializa o contador de divisores encontrados.
# Começa em 1 porque assume-se que todo número maior que 1 já é divisível por si mesmo.
cont = 1

# Inicializa a variável 'x' que será o testador de divisores, começando do número 1.
x = 1

# Loop (laço de repetição) que vai testar todos os números de 1 até o valor da raiz quadrada
while x <= raiz_primo:
    # Verifica se o resto da divisão de 'primo' por 'x' é igual a zero (ou seja, se 'x' é um divisor de 'primo')
    if primo % x == 0:
        # Se for um divisor exato, incrementa o contador de divisores em 1
        cont += 1

    # Avança para o próximo número a ser testado na próxima volta do loop
    x += 1

# Após o loop, faz a verificação final:
# Se o 'cont' for exatamente 2 (divisível por 1 e pela raiz, caso ela seja exata, ou outro par divisor)
# E o número for maior que 1 (já que 0 e 1 não são primos).
if cont == 2 and primo > 1:
    print(f"{n} é primo!")
else:
    print(f"{n} não é primo!")
