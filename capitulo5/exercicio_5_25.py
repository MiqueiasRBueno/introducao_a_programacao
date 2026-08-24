# Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de Newton para obter um resultado
# aproximado. Sendo n o número a obter a raiz quadrada, considere a base = 2. Calcule p usando a fómula p=(b+(n/b))/2.
# Agora calcule o quadrado de p. A cada passo, faça b=p e recalcule p usando a fórmula apresentada, Pare quando a
# diferença absoluta entre n e o quadrado de p for menor que 0,0001.

n_raiz = int(input("Insira um número inteiro para obter a raiz quadrada: "))
b = 2
while abs(n_raiz -(b * b)) > 0.0001:
    p = (b +(n_raiz/b)) / 2
    b = p
print(f"A raiz quadrada de {n_raiz} é aproximadamente {p:8.4f}")
