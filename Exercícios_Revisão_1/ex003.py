# 3. Faça um Programa que pergunte em que turno você estuda. Peça para
# digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o
# caso

turno = input("digite seu truno de estudo (M-matutino ou V-Vespertino ou N- Noturno): ")

if turno == "M":
    print("Bom dia")
elif turno == "V":
    print("Boa tarde")
elif turno == "N":
    print("Boa noite")
else:
    print("Valor invalido")