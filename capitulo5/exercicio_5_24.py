# Modifique o programa anterior de forma a ler um número n.
# Imprima os n primeiros números primos.

n = int(input("Insira um número: "))
if n < 0 or n == 0 or n == 1:
    print(f"{n} não é primo, números primos são números naturais maiores que 1 divisiveis por 1 e por eles mesmos!")
else:
    dividendo = 2
    while dividendo <= n:
        divisor = 1
        cont_zero = 1
        while divisor <= n:
            divisor += 1
            if dividendo % divisor == 0:
                cont_zero += 1
        if cont_zero > 2: print(f"{dividendo} não é primo.")
        else: print(f"{dividendo} é um número primo.")
        dividendo += 1
