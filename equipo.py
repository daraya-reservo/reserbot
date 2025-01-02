from settings import RUTA_PROYECTO
import json


integrantes_equipo = [
    {
        "nombre": "Agust\u00edn",
        "tag": "@apradenas",
        "dailies": 0,
        "disponible": True
    },
    {
        "nombre": "Dani",
        "tag": "@daraya",
        "dailies": 1,
        "disponible": True
    },
    {
        "nombre": "Hiho",
        "tag": "@ndelgado",
        "dailies": 1,
        "disponible": True
    },
    {
        "nombre": "Juan",
        "tag": "@jecclefield",
        "dailies": 1,
        "disponible": True
    },
    {
        "nombre": "Lucho",
        "tag": "@lpinochet",
        "dailies": 1,
        "disponible": True
    },
    {
        "nombre": "Manu",
        "tag": "@mgrandon",
        "dailies": 1,
        "disponible": True
    },
    {
        "nombre": "Nach",
        "tag": "@imachuca",
        "dailies": 1,
        "disponible": True
    },
    {
        "nombre": "Pancho",
        "tag": "@fvilla",
        "dailies": 1,
        "disponible": True
    },
    {
        "nombre": "Pato",
        "tag": "@ptapia",
        "dailies": 0,
        "disponible": True
    },
    {
        "nombre": "Seba",
        "tag": "@sconcha",
        "dailies": 1,
        "disponible": True
    },
    {
        "nombre": "Val",
        "tag": "@vgutierrez",
        "dailies": 1,
        "disponible": True
    },
    {
        "nombre": "Vicky",
        "tag": "@vmartinez",
        "dailies": 0,
        "disponible": True
    }
]

def get_integrantes_equipo(solo_disponibles=False, de_vacaciones=False):
    global integrantes_equipo
    # filtro los integrantes disponibles
    if solo_disponibles:
        integrantes_equipo = [integrante for integrante in integrantes_equipo if integrante['disponible']]
    elif de_vacaciones:
        integrantes_equipo = [integrante for integrante in integrantes_equipo if not integrante['disponible']]
    return integrantes_equipo

def update_integrantes_equipo(integrantes):
    global integrantes_equipo
    integrantes_equipo = integrantes