# Standard Library
import csv
import random

# Reserbot
import equipo
import settings


def es_dia_habil(dia):
    # si el día es sábado(5) o domingo(6)
    if dia.weekday() in [5, 6]:
        return False
    # abro archivo de feriados
    ruta_archivo_feriados = f'{settings.RUTA_PROYECTO}/csv/publicholiday.CL.{dia.year}.csv'  # ver README
    archivo_feriados = open(ruta_archivo_feriados)
    feriados = csv.DictReader(archivo_feriados)
    archivo_feriados.close()
    # chequea que el dia no esté en lista de feriados
    dia_format = dia.strftime('%Y-%m-%d')
    lista_feriados = [feriado['Date'] for feriado in feriados]
    return dia_format not in lista_feriados

def update_dailies(integrante_tag):
    integrantes_equipo = equipo.get_integrantes_equipo()
    for integrante in integrantes_equipo:
        if integrante['tag'] == integrante_tag:
            integrante['dailies'] += 1
            break
    equipo.update_integrantes_equipo(integrantes_equipo)

def update_disponibilidad(integrante_tag):
    integrantes_equipo = equipo.get_integrantes_equipo()
    for integrante in integrantes_equipo:
        if integrante['tag'] == integrante_tag:
            integrante['disponible'] = not integrante['disponible']
            break
    equipo.update_integrantes_equipo(integrantes_equipo)

def get_lider():
    integrantes_disponibles = equipo.get_integrantes_equipo(solo_disponibles=True)
    # lidera el que tenga menor numero de dailies lideradas
    random.shuffle(integrantes_disponibles)
    lider = min(integrantes_disponibles, key=lambda i:i['dailies']).get('tag')
    return lider['tag']

integrantes_aux = equipo.get_integrantes_equipo(solo_disponibles=True)

def get_lider_al_azar():
    global integrantes_aux
    try:
        lider_al_azar = random.choice(integrantes_aux)
    except IndexError:  # cuando integrantes_aux está vacia
        return None
    integrantes_aux.remove(lider_al_azar)
    return lider_al_azar['nombre']
