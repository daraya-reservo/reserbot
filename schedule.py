from datetime import datetime
import locale
import pytz
import settings
import slack_client
import utils

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
today = datetime.now(pytz.timezone('America/Santiago'))
daily_leader = utils.get_daily_leader(today)

if daily_leader:
    slack_client.schedule(
        channel='#reservo-ti',
        post_at=(today.replace(hour=9, minute=9 if today.weekday()!=2 else 30, second=0)).strftime('%s'),
        text=f'Hoy {today.strftime("%A %d")} lidera {daily_leader} :rubyrun:'
    )
    buttons = [
        {
            "text": "Meet :meet:",
            "url": settings.URL_MEET,
        },
        {
            "text": "Tablero :trello:",
            "url": settings.URL_TRELLO,
        }
    ]
    slack_client.schedule(
        channel='#reservo-ti',
        post_at=(today.replace(hour=9, minute=10 if today.weekday()!=2 else 31, second=0)).strftime('%s'),
        buttons=buttons,
    )
