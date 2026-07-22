# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h,
# exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa,
# cobrando R$ 5 por km acima de 80 km/h.

velocidade = int(input("Insira a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado!")
    print("Valor total da multa R$ %5.2f" %multa)
if velocidade <= 80:
    print("Você está  a %d km/h, parabéns dentro da velocidade permitida" %velocidade)
