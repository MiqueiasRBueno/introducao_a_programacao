# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

ent_metros = float(input("Digite um valor em metros: "))
conver_m_mm = ent_metros * 1000
print(f"{ent_metros:.2f} metros são {conver_m_mm:.2f} milímetros!")
