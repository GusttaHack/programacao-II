# 6. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da
# pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
# deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?"
]

respostas = []

for p in perguntas:
    resp = input(p)
    respostas.append(resp)

quant = respostas.count("s")
print(quant)

if quant == 2:
    print("Suspeito")
elif 3 >= quant < 5:
    print("Cumplice")
elif quant == 5:
    print("Assassino")
elif quant == 0:
    print("Inocente")
