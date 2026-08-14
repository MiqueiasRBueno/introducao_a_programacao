# Modifique o programa para aceitar valores decimais, ou seja, também contar moedas de 0,01 0,02 0,05 0,10 e 0,50

valor = float(input("Digite o valor a pagar: ")) * 100
cedulas = 0
atual = 10000
apagar = int(round(valor))
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédula(s) de R$ {atual/100:.2f}')
        if apagar <= 0:
            break
        elif atual == 10000:
            atual = 5000
        elif atual == 5000:
            atual = 2000
        elif atual == 2000:
            atual = 1000
        elif atual == 1000:
            atual = 500
        elif atual == 500:
            atual = 200
        elif atual == 200:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 25
        elif atual == 25:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
