# 1. Crie um programa em Python que peça dois números ao usuário. Em
# seguida, você vai mostrar a soma, subtração, multiplicação, divisão,
# exponenciação e resto da divisão do primeiro número pelo segundo.

n1 = float(input("insira um numero"))
n2 = float(input("insira um numero"))

soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
expo = n1**n2
resto = n1%n2

print(f"a soma:{soma}, a subtração {sub}, a multiplicação{multi}, a divisão{div}, a exponenenciação {expo}, o resto é: {resto}")