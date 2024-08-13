# 5. Faça um programa que peça um número inteiro e determine se ele é ou não
# um número primo. Um número primo é aquele que é divisível somente por ele
# mesmo e por 1.

num_int = int(input("Digite um numero inteiro: "))

if num_int%num_int == 0 and num_int%1 == 0:
    print(f"O numero {num_int} é um numero primo")
else:
    print(f"O numero {num_int} não é primo")