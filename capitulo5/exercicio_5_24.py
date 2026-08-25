# Modifique o programa anterior de forma a ler um número n.
# Imprima os n primeiros números primos.

# PASSO 1: Captura a quantidade de números primos que o usuário deseja ver
quant_n_primos = int(input("Insira um número para mostrar a quantidade de números primos: "))

# Guarda o valor digitado para usar como meta no nosso laço de repetição
quant_desejada = quant_n_primos

# Cria um contador para rastrear quantos números primos já encontramos e exibimos
quant_primos_encontrados = 0

# Define o primeiro número a ser testado. Começamos pelo 2 porque ele é o menor número primo
numero_atual = 2

# LOOP PRINCIPAL: O programa vai rodar enquanto não encontrarmos a quantidade de primos que o usuário pediu
while quant_primos_encontrados < quant_desejada:

    # Para cada novo 'numero_atual', precisamos começar testando a divisão a partir do número 2
    divisor = 2

    # Criamos uma "bandeira" (flag). Assumimos que o número É primo até que se prove o contrário
    e_primo = True

    # LOOP INTERNO: Vai testar todos os divisores possíveis para o 'numero_atual'
    # Ele testa desde o 2 até o número imediatamente anterior ao 'numero_atual'
    while divisor < numero_atual:

        # O operador '%' pega o resto da divisão.
        # Se o resto for ZERO, significa que o 'numero_atual' é divisível pelo 'divisor'
        if numero_atual % divisor == 0:
            # Se dividiu por alguém além de 1 e dele mesmo, descobrimos que ele NÃO é primo
            e_primo = False

        # Aumentamos o divisor em +1 para testar o próximo número no próximo ciclo deste loop
        divisor += 1

    # DEPOIS DE TESTAR TODOS OS DIVISORES: Verificamos se a nossa "bandeira" continuou True
    if e_primo == True:
        # Se ela continuou True, significa que nenhum divisor conseguiu quebrar o número. Ele é primo!
        print(numero_atual)  # Mostra o número primo na tela

        # Como encontramos um primo válido, aumentamos o nosso contador de primos encontrados
        quant_primos_encontrados += 1

    # Independentemente de ter sido primo ou não,
    # avançamos para o próximo número da sequência (ex: de 2 para 3, de 3 para 4...)
    numero_atual += 1
