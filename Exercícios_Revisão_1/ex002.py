# 2. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ["a","e","i","o","u"]
letra = input(f" digite uma letra: ")

if letra in vogais:
    print(f"a letra ({letra}) é uma vogal!")
else:
    print(f"a letra ({letra}) Não é uma vogal")


