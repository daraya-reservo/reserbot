# Reserbot
import settings

# Standard Library
import json


ruta_json = f'{settings.RUTA_PROYECTO}/equipo.json'

def get_integrantes_equipo(solo_disponibles=False, de_vacaciones=False):
    # abro archivo de integrantes del equipo
    json_equipo = open(ruta_json)
    integrantes_equipo = json.load(json_equipo)
    json_equipo.close()
    # aplico filtros
    if solo_disponibles:
        integrantes_equipo = [integrante for integrante in integrantes_equipo if integrante['disponible']]
    elif de_vacaciones:
        integrantes_equipo = [integrante for integrante in integrantes_equipo if not integrante['disponible']]
    return integrantes_equipo


def update_integrantes_equipo(integrantes_equipo):
    integrantes_equipo = json.dumps(integrantes_equipo, indent=4)
    json_equipo = open(ruta_json, 'w')
    json_equipo.write(integrantes_equipo)
    json_equipo.close()
