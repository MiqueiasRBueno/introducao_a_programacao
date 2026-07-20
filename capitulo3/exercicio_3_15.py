# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá.
# Exiba o total em dias.

quant_cigarros_dia = int(input("Insira a quantidade de cigarros fumados por dia: "))
anos_fumando = round(float(input("Insira a quantidade de anos fumando: ")), 2) * 365.25
min_perdidos = ((quant_cigarros_dia * 10) * anos_fumando) // 1440
print(f"Se você fuma {quant_cigarros_dia} cigarros por dia e fumou por {int(anos_fumando / 365.25)} anos ")
print(f"Se você perde 10 minutos de vida por cigarro fumado.")
print(f"Você perderá {min_perdidos:.0f} dias de vida ")
