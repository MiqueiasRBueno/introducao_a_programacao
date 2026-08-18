# Escreva um programa que leia um número e verifique se ele é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos
# os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero,
# o número não é primo. Observe que 0 e 1 não são primos e que 2 é o únoco número par que é primo.

# 1. Entrada de dados: Pede um número ao usuário e o converte para inteiro (int)
num_primo = int(input("Insira um número "))

# Cria uma cópia do valor para usar nos cálculos (boa prática para preservar o valor original)
num = num_primo

# 2. Validação inicial: Números menores ou iguais a 1 não são primos (ex: 0, 1 e negativos)
if num <= 1:
    primo = False  # Define a condição como falsa se cair aqui
else:
    primo = True  # Caso contrário, assumimos temporariamente que ele é primo

# 3. Otimização matemática: Não precisamos testar todos os números até 'num'.
# Se um número tem um divisor, pelo menos um deles é menor ou igual à sua raiz quadrada.
# Exemplo: para saber se 25 é primo, basta testar até a raiz de 25 (que é 5).
limite = int(num ** 0.5)

# 4. Laço de repetição: Testa os divisores começando do 2 até o limite calculado.
# Adicionamos +1 no 'limite + 1' porque a função range() exclui o último número.
for v in range(2, limite + 1):

    # Se o resto da divisão de 'num' por 'v' for igual a zero, significa que a divisão é exata
    if num % v == 0:
        primo = False  # Encontrou um divisor, logo, o número NÃO é primo
        break  # Interrompe o laço imediatamente para poupar processamento

# 5. Resultado final: Verifica o estado da variável booleana 'primo' e exibe a mensagem
if primo:
    print(f"{num_primo} é primo.")
else:
    print(f"{num_primo} não é primo.")
