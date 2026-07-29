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
resultado = 0
if operacao_escolhida == 1:
    resultado = numero_float_operacao_1 + numero_float_operacao_2
elif operacao_escolhida == 2:
    resultado = numero_float_operacao_1 - numero_float_operacao_2
elif operacao_escolhida == 3:
    resultado = numero_float_operacao_1 * numero_float_operacao_2
elif operacao_escolhida == 4:
    resultado= numero_float_operacao_1 / numero_float_operacao_2
else:
    print("Opção inválida!")
print(f"Resultado : {resultado:.2f}")
