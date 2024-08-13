# 12.Faça um programa que, dado um conjunto de N números, determine o menor
# valor, o maior valor e a soma dos valores.

resp = "s"
numeros = []

while resp == "s":
    num = int(input("Digite um numero: "))
    numeros.append(num)
    resp = input("Quer digitar outro numero?")

print(numeros)
print(f"O menor valor é: {min(numeros)}\nO maior valor é: {max(numeros)}\nA soma de todos os valores é: {sum(numeros)} ")