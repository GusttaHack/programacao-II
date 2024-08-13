# 4. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
# se a mesma é uma data válida.

data = input("Digite uma data(dd/mm/aaaa):")

dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

print(dia)
print(mes)
print(ano)

if ano > 0:
    if (ano%4 == 0 ) and (mes > 0 and mes <13) and (dia > 0 and dia < 32):
        if dia == 29 and mes == 2: 
            print("Ano bisexto válido")
        else:
            print("ano inválido")
    elif (ano%4 == 0) and (mes > 0 and mes < 13) and (dia > 0 and dia < 32):
        print("Ano válido")
    else:
        print("Ano inválido")
else:
    print("ano inválido")
