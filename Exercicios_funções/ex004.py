# 4. Crie um programa de câmbio. Nesse programa adicione funções que
# realizem conversões de real para dólar, real para euro e real para peso
# argentino, conforme o nome do país fornecido pelo usuário. Utilize os valores:
# 1,00 real = 0,18 dólar para Estados Unidos;
# 1,00 real = 0,16 euro para Portugal;
# 1,00 real = 170,54 peso para Argentina;

def dolar(n1):
    dolar = n1 * 0.18
    print(dolar)

def euro(n1):
    euro = n1 * 0.17
    print(euro)

def peso(n1):
    peso = n1 * 170.85
    print(peso)

pais = input("Digite o pais para o cambio:\nestado unidos, portugal, argentina:")

if pais == "estados unidos":
    dolar(float(input("Digite um valor para converter em dólar americano: ")))
elif pais == "portugal":
    euro(float(input("Digite um valor para converter em euro: ")))
elif pais == "argentina":
    peso(float(input("Digite um valor para converter em peso argentino: ")))







