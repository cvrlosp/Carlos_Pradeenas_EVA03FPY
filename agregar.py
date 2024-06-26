import json
import csv

def agregar(jsonf):
    if not jsonf.exists():
        jsonf.touch()
        print('El archivo no existia, pero ya fue creado')
    if jsonf.stat().st_size == 0:
        json_file = []
        codigo = [380560]
    else:
        with open(jsonf, mode= 'r') as stream:
            json_file = json.load(stream)
            codigo = []
            for pintura in json_file:
                codigo.append(pintura['CODIGO'])
            codigo = max(codigo) + 1 