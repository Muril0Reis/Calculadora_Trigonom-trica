import math
from utils import validar_entrada

def calcular_distancia():
    print("\n=== Cálculo de Distâncias ===")
    cateto1 = validar_entrada("Informe o comprimento do primeiro lado (cateto): ")
    cateto2 = validar_entrada("Informe o comprimento do segundo lado (cateto): ")
    
    if cateto1 is None or cateto2 is None:
        return
    
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    print(f"Comprimento da hipotenusa: {hipotenusa:.2f}")

def calcular_angulos():
    print("\n=== Cálculo de Ângulos ===")
    lado = validar_entrada("Informe o comprimento do lado conhecido: ")
    angulo_graus = validar_entrada("Informe o valor do ângulo (em graus): ")
    
    if lado is None or angulo_graus is None or angulo_graus >= 90:
        print("Lados devem ser positivos e ângulos devem estar entre 0 e 90 graus!")
        return
    
    angulo_radianos = math.radians(angulo_graus)
    hipotenusa = lado / math.sin(angulo_radianos)
    outro_lado = math.sqrt(hipotenusa**2 - lado**2)
    
    print(f"Comprimento dos lados: {lado:.2f}, {outro_lado:.2f}, {hipotenusa:.2f}")
    print(f"Ângulos do triângulo: {angulo_graus:.2f}°, {90 - angulo_graus:.2f}°, 90°")
