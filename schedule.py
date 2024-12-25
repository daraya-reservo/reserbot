from datetime import datetime
import locale
import pytz
import settings
import slack_client
import utils

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
hoy = datetime.now(pytz.timezone('America/Santiago'))

if utils.es_dia_habil(hoy):
    slack_client.schedule_message(
        channel=settings.CHANNEL_TESTING,
        post_at=(hoy.replace(hour=9, minute=0, second=0)).strftime('%s'),
        text=f'Hoy {hoy.strftime("%A %d")} lidera la daily {utils.get_lider_daily()} :goodmorning:',
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
