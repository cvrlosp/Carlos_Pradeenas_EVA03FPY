'''
Creacion del menu principal
'''

def construir_menu(lista):
    '''
    Crea un menu con el formato iterable +1. elemento
    '''
    for ind, opt in enumerate(lista):
        print(f'{ind +1}. {opt}')


def sol_ans():
    '''
    Pide una respuesta la guarda y la devuelve al ambiente global
    '''
    resp = input('¿Que quieres hacer?\n')
    return resp