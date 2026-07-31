# Reescreva o programa a seguir com if-elif-else.
#hora = int(input("Digite a hora atual:"))
# if hora < 12:
#     print("Bom dia!")
# if hora >=12 and hora <=18:
#     print("Boa tarde!")
# if hora >=18:
#      print("Boa noite!")

hora = int(input("Digite a hora atual: "))
if hora < 12: print("Bom dia!")
elif 12 < hora <= 18: print("Boa tarde!")
else: print("Boa noite!")
