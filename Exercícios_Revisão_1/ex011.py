# 11. Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

for c in range(n1,n2 + 1):
    if c != n2:
        print(c,end=", ")
    else:
        print(c,end="")

