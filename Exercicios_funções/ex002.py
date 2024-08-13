# 2. Faça um programa que calcule a área de um terreno e imprima na tela

def area(n1,n2):
    area = n1*n2
    print(f"a area do seu terreno é {area}")

n1 = float(input("Qual a largura do seu terreno? "))
n2 = float(input("Qual a comprimento do seu terreno? "))

area(n1,n2)