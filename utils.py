import csv
import json
import random
from settings import RUTA_PROYECTO
import integrantes_equipo as gggg


def es_dia_habil(dia):
    # si el día es sábado(5) o domingo(6)
    if dia.weekday() in [5, 6]:
        return False
    # abro archivo de feriados
    ruta_archivo_feriados = f'{RUTA_PROYECTO}/csv/publicholiday.CL.{dia.year}.csv'  # ver README
    archivo_feriados = open(ruta_archivo_feriados)
    feriados = csv.DictReader(archivo_feriados)
    archivo_feriados.close()
    # chequea que el dia no esté en lista de feriados
    dia_format = dia.strftime('%Y-%m-%d')
    lista_feriados = [feriado['Date'] for feriado in feriados]
    return dia_format not in lista_feriados

def get_integrantes_equipo(solo_disponibles=False, de_vacaciones=False):
    print(gggg)
    # abro archivo de integrantes del equipo
    json_equipo = open(f'{RUTA_PROYECTO}/integrantes_equipo.json')
    integrantes_equipo = json.load(json_equipo)
    json_equipo.close()
    # filtro los integrantes disponibles
    if solo_disponibles:
        integrantes_equipo = [integrante for integrante in integrantes_equipo if integrante['disponible']]
    elif de_vacaciones:
        integrantes_equipo = [integrante for integrante in integrantes_equipo if not integrante['disponible']]
    return integrantes_equipo

def update_dailies(integrante_tag):
    integrantes_equipo = get_integrantes_equipo()
    for integrante in integrantes_equipo:
        if integrante['tag'] == integrante_tag:
            integrante['dailies'] += 1
            break
    
    _update_equipo(integrantes_equipo)

def update_disponibilidad(integrante_tag):
    integrantes_equipo = get_integrantes_equipo()
    for integrante in integrantes_equipo:
        if integrante['tag'] == integrante_tag:
            integrante['disponible'] = not integrante['disponible']
            break
    for integrante in gggg:
        if integrante['tag'] == integrante_tag:
            integrante['disponible'] = not integrante['disponible']
            break
    _update_equipo(integrantes_equipo)

def _update_equipo(integrantes_equipo):
    integrantes_equipo = json.dumps(integrantes_equipo, indent=4)
    json_equipo = open(f'{RUTA_PROYECTO}/integrantes_equipo.json', 'w')
    json_equipo.write(integrantes_equipo)
    json_equipo.close()

def get_lider():
    integrantes_disponibles = get_integrantes_equipo(solo_disponibles=True)
    # lidera el que tenga menor numero de dailies lideradas
    random.shuffle(integrantes_disponibles)
    lider = min(integrantes_disponibles, key=lambda i:i['dailies']).get('tag')
    return lider['tag']

integrantes_aux = get_integrantes_equipo(solo_disponibles=True)

def get_lider_al_azar():
    global integrantes_aux
    try:
        lider_al_azar = random.choice(integrantes_aux)
    except IndexError:  # cuando integrantes_aux está vacia
        return None
    integrantes_aux.remove(lider_al_azar)
    return lider_al_azar['nombre']
