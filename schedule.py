from datetime import datetime, timedelta
import settings
import slack_client
import utils


today = datetime.now()
lider_daily = utils.lider_daily()
daily_leader = utils.get_daily_leader()
print('------------PROBANDO FUNCION DAILY NUEVA-------------')
print('today: ', today.strftime('%A %d'))
print('lider daily primera forma: ', lider_daily)
print('team antes: ', utils.get_team() )
print('lider daily segunda forma: ', daily_leader)
print('team despues: ', utils.get_team() )
print('------------PROBANDO FUNCION DAILY NUEVA-------------')

if lider_daily:
    slack_client.schedule(
        channel='#reserbot-shhhh',
        post_at=(today.replace(hour=9, minute=35, second=0)).strftime('%s'),
        text=f'Hoy {today.strftime("%A %d")} lidera {daily_leader} :rubyrun:'
    )
    slack_client.schedule(
        channel='#reservo-ti',
        post_at=(today.replace(hour=9, minute=35, second=0)).strftime('%s'),
        text=f'Hoy {today.strftime("%A %d")} lidera {lider_daily} :finoseñores:',
    )
    buttons = [
        {
            "text": "Daily :discord2:",
            "url": settings.URL_DISCORD,
        },
        {
            "text": "Abrir Tablero :trello:",
            "url": settings.URL_TRELLO,
        }
    ]
    slack_client.schedule(
        channel='#reservo-ti',
        post_at=(today.replace(hour=9, minute=50, second=0)).strftime('%s'),
        buttons=buttons,
    )

if today.weekday() == 0:
    first_workday = today if utils.is_working_day(today) else today + timedelta(days=1) 
    slack_client.schedule(
        channel='#reserbot-shhhh',
        post_at=(first_workday.replace(hour=10, minute=30, second=0)).strftime('%s'),
        buttons=[{
            'text': 'Leer newsletter',
            'url': settings.URL_NEWSLETTERS
        }]
    )
else:
    slack_client.schedule(
        channel='#reserbot-shhhh',
        post_at=(today.replace(hour=10, minute=30, second=0)).strftime('%s'),
        buttons=[{
            'text': f'Hoy {today.strftime("%s")} no es lunes ni martes',
            'url': settings.URL_NEWSLETTERS
        }]
    )