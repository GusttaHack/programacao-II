from functions import *

nome = saudacao()

resp = "sim"

while resp == "sim":
    conversão = input(f"Qual conversão deseja fazer {nome}?\nComprimento, Volume, Massa, Area ou Temperatura: /n").lower()
    if conversão == "comprimento":
        Comprimento()
        pass
    elif conversão == "volume":
        Volume()
        pass
    elif conversão == "massa":
        Massa()
        pass
    elif conversão == "temperatura":
        Temperatura()
        pass
    elif conversão == "area":
        Area()
        pass
    resp = input("Quer fazer uma nova conversão?")
