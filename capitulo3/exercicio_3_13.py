# Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:
#      9 × C
#  F = ----- + 32
#        5

temp_celsius = round(float(input("Insira a temperatura em graus célsius: ")),1)
temp_fahrenheit = (9 * temp_celsius)/ 5 + 32
print(f"A temperatura {temp_celsius}°C")
print(f"Em Fahrenheit é {temp_fahrenheit:.1f}°F")
