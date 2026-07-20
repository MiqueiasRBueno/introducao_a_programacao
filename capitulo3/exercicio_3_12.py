# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dist_percorrer = round(float(input("Qual a distância a percorrer?: ")),2)
vel_media = int(input("Qual a velocidade média estimada?: "))
temp_total =  dist_percorrer / vel_media
mint_total = (temp_total - int(temp_total)) * 60
print("A uma velocidade média de %dkm/h" %vel_media)
print("Você percorrerá a distância de %5.2fkm" %dist_percorrer)
print(f"Em {int(temp_total)}h{int(mint_total)}min")