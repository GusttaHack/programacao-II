# 2. Crie um sistema para um aplicativo bancário, que possui a Classe
# ContaBancaria com as seguintes características:
# ○ Atributos: titular, saldo, numero_conta e tipo_conta.
# ○ Métodos: depositar, sacar, transferir e verificar_saldo.
# OBS: Após cada alteração no saldo, exiba o novo valor na tela.

class contabancaria():
    def __init__(self, titular, saldo, numero_conta, tipo_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta

        print(f"Você tem R${saldo:.2f} na sua conta.\n")

    def depositar(self):
        valor = float(input("Digite o valor para ser depositado:"))
        self.saldo += valor
        print(f"você depositou R${valor:.2f}\nSeu saldo:R${self.saldo:.2f}\n")

    def sacar(self):
        valor = float(input("Digite o valor para sacar:"))
        self.saldo -= valor
        print(f"você sacou R${valor:.2f}\nSeu saldo:R${self.saldo:.2f}")

    def transferir(self):
        banco = 1000
        print(f"Saldo do Banco: R${banco:.2f}\n")
        valor = float(input(f"Quanto você que transferir para sua conta? "))
        banco -= valor
        self.saldo += valor
        print(f"você transferiu R${valor:.2f} do banco para sua conta\nSaldo do Banco: R${banco:.2f}\nSeu saldo:R${self.saldo:.2f}\n")
    
    def verificar_saldo(self):
        print(f"Seu saldo atual é R${self.saldo:.2f}.\n")


    def realizar_operacao(self):
        resp = "sim"
        while resp == "sim":
            operacao = input("O que deseja fazer?\nDepositar(1): \nSacar(2): \nTransferir(3): \nVerificar Saldo(4): \nSair(0): ")
            print()
            if operacao == "1":
                self.depositar()
            elif operacao == "2":
                self.sacar()
            elif operacao == "3":
                self.transferir()
            elif operacao == "4":
                self.verificar_saldo()
            elif operacao == "0":
                print("Programa finalizado!")
                break
            else:
                print("operação inválida!,tente novamente")

conta = contabancaria("Gustavo",10000,"883481", "CC")

conta.realizar_operacao()