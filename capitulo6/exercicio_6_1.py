# Modifique o Programa 6.2 para ler 7 notas em vez de 5.

notas = [0, 0, 0, 0, 0, 0, 0,]
soma = x = 0
while x < 7:
    notas[x] = float(input(f"Insira a {x + 1}ª nota: "))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print(f"{x + 1}ª nota: {notas[x]:6.2f}")
    x += 1
print(f"Média: {soma / x:6.2f}")