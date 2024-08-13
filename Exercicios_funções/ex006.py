# 6. Faça um programa que converta da notação de 24 horas para a notação de 12
# horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é
# dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
# conversão e uma para personalizar a saída.

def converter():
    horario = input("Digite a hora que deseja converter(ex, 12:12):")
    hora = int(horario[:2])
    min = int(horario[3:])
    periodo = ""
    if 0 < min < 59:
        if 0 <= hora < 1:
            hora += 12
            periodo = "AM"
            return hora,min,periodo
        elif 1 <= hora <= 12:
            periodo = "AM"
            return hora,min,periodo
        elif 13 <= hora <= 23:
            hora -= 12
            periodo = "PM"
            return hora,min,periodo
        else:
            print("Digite uma hora válida!")

    else:
        print("Digite um minuto válido!")

def formatar(horario):
    horario = list(horario)
    hora = horario[0]
    minuto = horario[1]
    tipo = horario[2]

    print(f"{hora}:{minuto}{tipo}")
    
horario = converter()

formatar(horario)
