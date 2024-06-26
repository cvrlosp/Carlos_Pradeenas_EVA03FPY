import json

def slt_code():
    '''
    Pide el codigo a eliminar y lo guarda
    '''
    code = input('Ingresa el codigo de la pintura que quieres eliminar\n')
    if code.isnumeric():
        return int(code)
    

def eliminar(dato, rutaj):
    if dato == None:
        print('El archivo no es compatible\n')
    else:
        with open(rutaj, mode= 'r') as stream:
            json_file = json.load(stream)
            for pintura in json_file:
                if pintura['CODIGO'] == dato:
                    json_file.remove(dato)
                    print('El archivo se ha eliminado correctamente\n')
            with open(rutaj, mode= 'w') as stream:
                json.dump(json_file, stream)