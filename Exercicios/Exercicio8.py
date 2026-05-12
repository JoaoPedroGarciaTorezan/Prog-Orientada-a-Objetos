import numpy as np

def Conversor_Farenheit(Celsius):
    F = 1.8 * Celsius + 32
    return F

temp_C = int(input("Informe a temperatura em Celsius: "))
print("Esta temperatura em Farenheit é: " + str(Conversor_Farenheit(temp_C)))