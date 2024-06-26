import json

def buscar(dato, jsonf):
    if not jsonf.exists():
        print('El archivo no existe\n')
    elif jsonf.stat().st_size == 0:
        print('El archivo esta vacio\n')
    else:
        with open(jsonf, mode= 'r') as stream:
            json_file = json.load(stream)
            for pintura in json_file:
                if str(pintura['CODIGO']) == dato or dato.upper() in pintura['CODIGO']:
                    print(f'Nombre: {pintura['Nombre']}')
                    print(f'Codigo: {pintura['Codigo']}')


def slt_vals():
    '''
    Pide una respuesta, la guarda una respuesta y la devuelve en el ambito global
    '''
    resp = input('Ingresa el nombre o el codigo de la pintura')
    return resp

