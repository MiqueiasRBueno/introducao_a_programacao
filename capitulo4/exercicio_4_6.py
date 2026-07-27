# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km e R$ 0,45 para viagens mais longas.

distancia_percorrer = int(input("Insira a distância que deseja percorrer: "))
total = 0
if distancia_percorrer > 200:
    total = distancia_percorrer * 0.45
else:
    total = distancia_percorrer * 0.5
print(f"Total a pagar por {distancia_percorrer} km: R$ {total:6.2f}")
