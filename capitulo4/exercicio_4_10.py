# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
#  Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). 
# Exiba o resultado da operação solicitada.
numero_float_operacao_1, numero_float_operacao_2 = map(float, input("Insira dois valores separados por um espaço: ").split())
print("""Escolha a operçaõ abaixo:

1 = soma
2 = subtração
3 = multiplicação
4 = divisão
""")
operacao_escolhida = int(input("Insira o número da operação desejada: "))
if operacao_escolhida == 1:
    print(f"A  soma entre {numero_float_operacao_1:.2f} e {numero_float_operacao_2:.2f}"
          f" é {numero_float_operacao_1 + numero_float_operacao_2:.2f}")
elif operacao_escolhida == 2:
    print(f"A  subtração entre {numero_float_operacao_1:.2f} e {numero_float_operacao_2:.2f} "
          f"é {numero_float_operacao_1 - numero_float_operacao_2:.2f}")
else:
    if operacao_escolhida == 3:
        print(f"A  multiplicação entre {numero_float_operacao_1:.2f} e {numero_float_operacao_2:.2f} "
                  f"é {numero_float_operacao_1 * numero_float_operacao_2:.2f}")
    elif operacao_escolhida == 4:
        print(f"A  divisão entre {numero_float_operacao_1:.2f} e {numero_float_operacao_2:.2f} "
                  f"é {numero_float_operacao_1 / numero_float_operacao_2:.2f}")
