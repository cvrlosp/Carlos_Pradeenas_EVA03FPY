import json
import csv

def exportar(rutaj, rutac):
    if not rutaj.exists() or rutaj.stat().st_size == 0:
        print('El archivo no existe o esta vacio\n')
    else:
        if not rutac.exists():
            rutac.touch()
        else:
            rutac.unlink()
            rutac.touch()
        with open(rutaj, mode= 'r') as stream:
            json_file = json.load(stream)
            for pintura in json_file:
                datos = [pintura ['CODIGO'],
                        pintura ['NOMBRE']]
                with open(rutac, mode= 'w') as cfile:
                    writer = csv.writer(cfile)
                    writer.writerow(datos)