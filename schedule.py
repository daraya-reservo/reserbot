from datetime import datetime
import locale
import pytz
import settings
import slack_client
from utils import get_lider_daily


locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
today = datetime.now(pytz.timezone('America/Santiago'))
lider_daily = get_lider_daily(today)

if lider_daily:
    slack_client.schedule_message(
        channel=settings.CHANNEL_TESTING,
        post_at=(today.replace(hour=9, minute=0, second=0)).strftime('%s'),
        text=f'Hoy {today.strftime("%A %d")} lidera {lider_daily} :rubyrun:'
    )
    slack_client.schedule_message(
        channel=settings.CHANNEL_TESTING,
        post_at=(today.replace(hour=9, minute=0, second=5)).strftime('%s'),
        buttons=[
            {
                "text": "Meet :meet:",
                "url": settings.URL_MEET,
            },
            {
                "text": "Tablero :trello:",
                "url": settings.URL_TRELLO,
            }
        ],
    )
