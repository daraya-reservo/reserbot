from datetime import datetime
import locale
import pytz
import settings
from bot_interface import programar_mensaje
import utils

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
hoy = datetime.now(pytz.timezone('America/Santiago'))

if utils.es_dia_habil(hoy):
    integrantes_no_disponibles = utils.get_integrantes_equipo(de_vacaciones=True)
    lider = utils.get_lider()
    programar_mensaje(
        channel=settings.TEST_ENV,
        post_at=(hoy.replace(hour=9, minute=0, second=0)).strftime('%s'),
        text=f'Hoy {hoy.strftime("%A %d")} lidera la daily {lider} :goodmorning:',
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
    )
