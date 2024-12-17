import csv
import json
import operator
import os
import random


def es_dia_festivo(dia):
    # si el día es sábado/domingo:
    if dia.weekday() in [5, 6]:
        return True
    # abro archvo de feriados
    ruta_proyecto = os.path.realpath(os.path.dirname(__file__))
    ruta_archivo_feriados = f'{ruta_proyecto}/csv/publicholiday.CL.{dia.year}.csv'  # ver README
    archivo_feriados = open(ruta_archivo_feriados)
    feriados = csv.DictReader(archivo_feriados)
    archivo_feriados.close()
    # chequea si el dia está en los feriados
    dia_format = dia.strftime('%Y-%m-%d')
    return dia_format in [feriado['Date'] for feriado in feriados]

def get_integrantes_equipo(solo_disponibles=False):
    # abro archivo de integrantes del equipo
    ruta_proyecto = os.path.realpath(os.path.dirname(__file__))
    json_equipo = open(f'{ruta_proyecto}/integrantes_equipo.json')
    integrantes_equipo = json.load(json_equipo)
    json_equipo.close()
    # filtro los integrantes disponibles
    if solo_disponibles:
        return [integrante for integrante in integrantes_equipo if integrante['disponible']]
    return integrantes_equipo

def update_dailies_equipo(tag_ultimo_lider):
    integrantes_equipo = get_integrantes_equipo()
    for integrante in integrantes_equipo:
        if integrante['tag'] == tag_ultimo_lider:
            integrante['dailies'] += 1
    integrantes_equipo = json.dumps(integrantes_equipo, indent=4)
    ruta_proyecto = os.path.realpath(os.path.dirname(__file__))
    json_equipo = open(f'{ruta_proyecto}/integrantes_equipo.json', 'w')
    json_equipo.write(integrantes_equipo)
    json_equipo.close()

def update_disponibilidad_equipo(tag_integrante):
    integrantes_equipo = get_integrantes_equipo()
    for integrante in integrantes_equipo:
        if integrante['tag'] == tag_integrante:
            integrante['disponible'] = not integrante['disponible']
    integrantes_equipo = json.dumps(integrantes_equipo, indent=4)
    ruta_proyecto = os.path.realpath(os.path.dirname(__file__))
    json_equipo = open(f'{ruta_proyecto}/integrantes_equipo.json', 'w')
    json_equipo.write(integrantes_equipo)
    json_equipo.close()

def update_team(team_as_list):
    project_path = os.path.realpath(os.path.dirname(__file__))
    team_as_json = json.dumps(team_as_list, indent=4)
    with open(f'{project_path}/team_data.json', 'w') as json_file:
        json_file.write(team_as_json)

def get_lider_daily(today):
    if es_dia_festivo(today):
       return None
    team = get_integrantes_equipo()
    members = list(team.items())
    random.shuffle(members)
    teammates = dict(sorted(dict(members).items(), key=operator.itemgetter(1)))
    daily_leader = next(iter(teammates))
    team[daily_leader] += 1
    update_team(team)
    return daily_leader

def get_lider_random(integrantes):
    lider = random.choice(integrantes)
    integrantes.remove(lider)
    return lider, integrantes

def build_message(text=None, buttons=None):
    message = []
    if text:
        message.append({
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': text
            }
        })
    if buttons:
        btn_elements = [{
            'type': 'button',
            'text': {
                'type': 'plain_text',
                'text': button['text'],
                'emoji': True
            },
            'style': 'primary',
            'url': button['url']
        } for button in buttons]
        message.append({
            'type': 'actions',
            'elements': btn_elements
        })
    return message