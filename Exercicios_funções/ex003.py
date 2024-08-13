# 3. Faça um programa que receba três números do usuário, e identifique o maior
# através de uma função e o menor número através de outra função.

def maior(n1,n2,n3):
    maior = 0
    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n1 and n2 > n3:
        maior = n2
    elif n3 > n1 and n3 > n2:
        maior = n3
    print(maior)

def menor(n1,n2,n3):
    menor = 0
    if n1 < n2 and n1 < n3:
        menor = n1
    elif n2 < n1 and n2 < n3:
        menor = n2
    elif n3 < n1 and n3 < n2:
        menor = n3
    print(menor)


n1 = float(input("Digite um valor: "))
n2 = float(input("Digite um valor: "))
n3 = float(input("Digite um valor: "))

maior(n1,n2,n3)
menor(n1,n2,n3)

