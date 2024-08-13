# 7. Crie uma função que receba um número indeterminado de valores inteiros e
# depois apresente a soma deles na tela. Use: def nome_da_funcao (* parametro):

def somadenumeros(*n1):
    nums = 0
    for i in n1:
        nums += i
    print(nums)

somadenumeros(1,2,3,4,5,6,3,1,2,3,5)
