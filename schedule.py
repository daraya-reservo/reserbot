from datetime import datetime, timedelta
import locale
import pytz
import settings
import slack_client
import utils


locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
today = datetime.now(pytz.timezone('America/Santiago'))
print('team antes: ', utils.get_team() )
daily_leader = utils.get_daily_leader(today)
print('lider daily: ', daily_leader)
print('team despues: ', utils.get_team() )

if daily_leader:
    slack_client.schedule(
        channel='#reserbot-shhhh',
        post_at=(today.replace(hour=9, minute=9, second=0)).strftime('%s'),
        text=f'Hoy {today.strftime("%A %d")} lidera {daily_leader} :rubyrun:'
    )
    buttons = [
        {
            "text": "Daily :discord2:",
            "url": settings.URL_DISCORD,
        },
        {
            "text": "Tablero :trello:",
            "url": settings.URL_TRELLO,
        }
    ]
    slack_client.schedule(
        channel='#reserbot-shhhh',
        post_at=(today.replace(hour=9, minute=10, second=0)).strftime('%s'),
        buttons=buttons,
    )
    if today.weekday() == 0:
        slack_client.schedule(
            channel='#reserbot-shhhh',
            post_at=(today.replace(hour=10, minute=30, second=0)).strftime('%s'),
            buttons=[{
                'text': 'Leer newsletter',
                'url': settings.URL_NEWSLETTERS
            }]
        )
