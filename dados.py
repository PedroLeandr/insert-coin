import json

def ler_temp():
    with open("data/temp.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)