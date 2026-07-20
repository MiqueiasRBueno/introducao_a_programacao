# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("segundos: "))
tot_seg_usuario = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(f"{tot_seg_usuario:.2f} segundos")
