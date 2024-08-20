from funções import *

def main():
    calc = Calculadora()
    while True:
        print("\nEscolha uma operação:\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Potência\n6. Raiz Quadrada\n7. Sair")
        escolha = input("Digite o número da operação desejada: ")
        if escolha == '7':
            print("Encerrando a calculadora...")
            break
        elif escolha == '6':
                num = float(input("Digite um número: "))
                resultado = calc.raiz_quadrada(num)
                inteiro, decimal = str(resultado).split(".")
                if int(decimal) > 0:
                    print(f"A raiz quadrada não exata de {num} é {resultado:.2f}")
                else:
                    print(f"A raiz quadrada de {num} é {int(resultado)}")
        elif escolha in ['1','2','3','4','5']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if escolha == '1':
                print(f"Resultado: {calc.soma(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {calc.subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {calc.multiplicacao(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {calc.divisao(num1, num2)}")
            elif escolha == '5':
                print(f"Resultado: {calc.potenciacao(num1, num2)}") 
        else:
            print("Opção inválida! Por favor, escolha uma operação válida.")
main()