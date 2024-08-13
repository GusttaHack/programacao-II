# 10.Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

validade = ""

while validade != "valido":
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))
    genero = input("Digite seu gênero:\nFeminino(f), Masculino(m): ").lower()
    estadocivil = input("Digite seu estado civil:\nSolteiro(s), Casado(c), viuvo(v), divorciado(d): ").lower()

    if len(nome) > 3 and 0 < idade < 150 and salario > 0 and (genero == "f" or genero == "m") and (estadocivil == "s" or estadocivil == "c" or estadocivil == "v" or estadocivil == "d"):
        validade = "valido"
        print("as informações solicitadas são validas")
    else:
        validade = "invalido"
        print("as informações solicitadas são invalidas")



