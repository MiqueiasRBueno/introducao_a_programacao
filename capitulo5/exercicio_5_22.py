# Escreva um programa que exiba uma lista de opções (menu):
# adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
# Repita até que a opção saída seja escolhida.

while True:
    print("""___Escolha a operação desejada na lista abaixo___
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair""")
    opcao = int(input("Escolha a operação: "))
    if 1 <= opcao < 5:
        n = 1
        tabuada = int(input("Tabuada de: "))
        while n <= 10:
            if opcao == 1:
                print(f'{n} + {tabuada} = {tabuada + n}')
            elif opcao == 2:
                print(f'{n + tabuada} - {tabuada} = {(n + tabuada) - tabuada}')
            elif opcao == 3:
                print(f'{n} x {tabuada} = {n * tabuada}')
            elif opcao == 4:
                print(f'{n * tabuada} ÷ {tabuada} = {(n * tabuada) / tabuada:.0f}')
            n += 1
    elif opcao == 5:
        print(f"Tabuada finalizada!")
        break
    else:
        opcao = int(input("Opção inválida, digite novamente: "))
