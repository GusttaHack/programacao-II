# 8. Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD.
# Escreva um programa que pergunta a situação do usuário (se é idoso, se é
# gestante, se é PCD ou nenhum destes) e diga se ele pode ter acesso a fila
# prioridade ou não.

situacao = input("Qual a sua situação?\nidoso, gestante ou PCD: ").lower()

if situacao == "idoso" or situacao == "gestante" or situacao == "pcd":
    print("Você tem direito a fila de prioridade!")
else:
    print("Você não tem direito a fila de prioridade!")