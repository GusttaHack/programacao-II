num_int = int(input("Digite um numero inteiro: "))

if num_int%num_int == 0 and num_int%1 == 0:
    print(f"O numero {num_int} é um numero primo")
else:
    print(f"O numero {num_int} não é primo")