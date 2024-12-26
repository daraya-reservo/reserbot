import csv
import json
import random
from settings import RUTA_PROYECTO


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

def get_integrantes_equipo(filtrar_disponibles=True):
    # abro archivo de integrantes del equipo
    json_equipo = open(f'{RUTA_PROYECTO}/integrantes_equipo.json')
    integrantes_equipo = json.load(json_equipo)
    json_equipo.close()
    # filtro los integrantes disponibles
    if filtrar_disponibles:
        integrantes_equipo = [integrante for integrante in integrantes_equipo if integrante['disponible']]
    return integrantes_equipo

def update_dailies_equipo(tag_integrante):
    integrantes_equipo = get_integrantes_equipo(filtrar_disponibles=False)
    for integrante in integrantes_equipo:
        if integrante['tag'] == tag_integrante:
            integrante['dailies'] += 1
    _update_equipo(integrantes_equipo)

def update_vacaciones(tag_integrante):
    integrantes_equipo = get_integrantes_equipo(filtrar_disponibles=False)
    for integrante in integrantes_equipo:
        if integrante['tag'] == tag_integrante:
            integrante['disponible'] = not integrante['disponible']
    _update_equipo(integrantes_equipo)

def _update_equipo(integrantes_equipo):
    integrantes_equipo = json.dumps(integrantes_equipo, indent=4)
    json_equipo = open(f'{RUTA_PROYECTO}/integrantes_equipo.json', 'w')
    json_equipo.write(integrantes_equipo)
    json_equipo.close()

def get_lider():
    integrantes_disponibles = get_integrantes_equipo(filtrar_disponibles=True)
    # lidera el que tenga menos dailies
    lider = integrantes_disponibles[0]
    for integrante in integrantes_disponibles:
        if integrante['dailies'] <= lider['dailies']:
            lider = integrante['dailies']
        elif integrante['dailies'] == lider['dailies']:
            lider = random.choice([lider, integrante])
    return lider['tag']

integrantes_aux = get_integrantes_equipo(filtrar_disponibles=True)

def get_lider_al_azar():
    global integrantes_aux
    lider_al_azar = random.choice(integrantes_aux)
    integrantes_aux.remove(lider_al_azar)
    return lider_al_azar['nombre']
