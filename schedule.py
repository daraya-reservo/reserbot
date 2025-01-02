# Standard library
from datetime import datetime
import locale

# Third Party
import pytz

# Reserbot
import settings
import bot
import utils

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
hoy = datetime.now(pytz.timezone('America/Santiago'))

if utils.es_dia_habil(hoy):
    # integrantes no disponibles
    integrantes_no_disponibles = utils.get_integrantes_equipo(de_vacaciones=True)
    if integrantes_no_disponibles:
        bot.programar_mensaje(
            post_at=(hoy.replace(hour=9, minute=0, second=0)).strftime('%s'),
            text=f'Hoy no estará: {", ".join(integrantes_no_disponibles)} :palmera:',
            debug=True
        )
    # integrante que lidera daily hoy
    lider = utils.get_lider()
    bot.programar_mensaje(
        post_at=(hoy.replace(hour=9, minute=2, second=0)).strftime('%s'),
        text=f'Hoy {hoy.strftime("%A %d")} lidera {lider} :shirabesleep: (recuerden actualizar sus tarjetas)',
        buttons=[
            {
                "text": "Link a Meet :meet:",
                "url": settings.URL_MEET,
            },
            {
                "text": "Link a Trello :trello:",
                "url": settings.URL_TRELLO,
            }
        ],
        debug=True
    )
    # recordatorio de actualizar tarjetas
    bot.programar_mensaje(
        post_at=(hoy.replace(hour=17, minute=50, second=0)).strftime('%s'),
        text='Recuerden actualizar sus tarjetas :rubyruntheotherway:',
        buttons=[{
            "text": "Link a Trello :trello:",
            "url": settings.URL_TRELLO,
        }],
        debug=True
    )
