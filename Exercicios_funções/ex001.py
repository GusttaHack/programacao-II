# 1. Escreva um código que receba o nome de uma pessoa e imprima uma
# saudação personalizada na tela com o nome do usuário

def saudacao(nome):
    print(f"Seja bem vindo, {nome}!")

saudacao(input("Qual o seu nome: ").capitalize())