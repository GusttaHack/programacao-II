# 5. Escreva um programa que possa cadastrar clientes ou funcionários para uma
# loja. Se o usuário quiser cadastrar um cliente, dados de nome, endereço,
# CPF devem ser solicitados. Caso o usuário prefira adicionar um novo
# funcionário, dados de nome, salário, cargo e CPF devem ser requisitados.
# Utilize comandos de manipulação de string para personalizar a saída.


def cadastro(tipo):
    if tipo == "cliente":
        cliente = []
        cliente.append(input("Digite o nome do cliente: "))
        cliente.append(input("Digite o endereço do cliente: "))
        cliente.append(input("Digite o CPF do cliente: "))
        print(f"voce cadatrou o cliente:{cliente[0]}\nEndereço {cliente[1]}\nCPF: {cliente[2]}")
    elif tipo == "funcionario":
        funcionario = []
        funcionario.append(input("Digite o nome do funcionario: "))
        funcionario.append(float(input("Digite o salario do funcionario: ")))
        funcionario.append(input("Digite o cargo do funcionario: "))
        funcionario.append(input("Digite o CPF do funcionario: "))
        print(f"voce cadatrou o funcionario:{funcionario[0]}\nSalario: {funcionario[1]}\nCargo: {funcionario[2]}\nCPF: {funcionario[3]}")

cadastro(input("Qual tipo de usuario voce deseja cadastrar?"))


    