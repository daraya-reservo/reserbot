# Standard library
from datetime import datetime
import locale

# Third Party
import pytz

# Reserbot
import settings
import slack_manager
import team_manager
import utils


locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
today = datetime.now(pytz.timezone('America/Santiago'))

if utils.is_workday(today):
    # integrantes no disponibles
    members_on_vacation = [
        member['name']
        for member in 
        team_manager.get_team(on_vacation=True)
    ]
    if members_on_vacation:
        text = f'Hoy no estará: {", ".join(members_on_vacation)} :shirabesleep:'
        post_at = (today.replace(hour=9, minute=0, second=0)).strftime('%s')
        slack_manager.schedule_message(
            post_at=post_at,
            text=text,
        )
    # integrante que lidera la daily hoy
    leader = utils.get_leader()
    text = f'Hoy {today.strftime("%A %d")} lidera {leader} :anime: (dejen comentario en sus tarjetas :bonk-doge: )'
    post_at = (today.replace(hour=9, minute=1, second=0)).strftime('%s')
    slack_manager.schedule_message(
        post_at=post_at,
        text=text,
        buttons=[
            {
                "text": "Abrir Trello :trello:",
                "url": settings.URL_TRELLO,
            },
            {
                "text": "Abrir Meet :meet:",
                "url": settings.URL_MEET,
            },
        ],
    )
    # recordatorio de actualizar tarjetas
    text = 'Dejen un comentario en sus tarjetas :homer-disappear:',
    post_at = (today.replace(hour=17, minute=50, second=0)).strftime('%s')
    slack_manager.schedule_message(
        post_at=post_at,
        text=text,
        buttons=[{
            "text": "Abrir Trello :trello:",
            "url": settings.URL_TRELLO,
        }],
    )
