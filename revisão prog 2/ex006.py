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
