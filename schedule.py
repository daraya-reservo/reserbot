from datetime import datetime
import locale
import pytz
import settings
from bot_interface import programar_mensaje
from utils import es_dia_habil, get_lider

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
hoy = datetime.now(pytz.timezone('America/Santiago'))

if es_dia_habil(hoy):
    hoy_formatted = hoy.strftime("%A %d")
    lider = get_lider()
    programar_mensaje(
        channel=settings.CHANNEL_TESTING,
        post_at=(hoy.replace(hour=9, minute=0, second=0)).strftime('%s'),
        text=f'Hoy {hoy_formatted} lidera la daily {lider} :goodmorning:',
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
