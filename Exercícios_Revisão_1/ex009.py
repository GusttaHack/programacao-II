# 9. Faça um programa que leia um nome de usuário e a sua senha e não aceite
# a senha igual ao nome do usuário, mostrando uma mensagem de erro e
# voltando a pedir as informações.

nick = ""
senha = ""

while nick == senha:
    nick = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if senha != nick:
        print(f"seu nome de usuário é {nick} e sua senha é {senha}")
        break