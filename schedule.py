from datetime import datetime
import locale
import pytz
import settings
import slack_client
import utils

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
hoy = datetime.now(pytz.timezone('America/Santiago'))
lider_daily = get_lider_daily(hoy)

if utils.es_dia_habil(hoy):
    lider = utils.get_lider_daily()
    slack_client.schedule_message(
        channel=settings.CHANNEL_TESTING,
        post_at=(hoy.replace(hour=9, minute=0, second=0)).strftime('%s'),
        text=f'Hoy {hoy.strftime("%A %d")} lidera {lider_daily} :rubyrun:',
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
