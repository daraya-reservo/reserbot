# Standard library
from datetime import datetime
import locale

# Third Party
import pytz

# Reserbot
import settings
from slack_manager import schedule_message
from team_manager import get_team
from utils import (
    is_workday,
    get_leader,
)


locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
today = datetime.now(pytz.timezone('America/Santiago'))

if is_workday(today):
    # integrantes no disponibles
    team_on_vacation = get_team(on_vacation=True)
    if team_on_vacation:
        text = f'Hoy no estará: {", ".join(team_on_vacation)} :palmera:'
        schedule_message(
            post_at=(today.replace(hour=9, minute=0, second=0)).strftime('%s'),
            text=text,
            debug=True
        )
    # integrante que lidera la daily hoy
    lider = get_leader()
    text = f'Hoy {today.strftime("%A %d")} lidera {lider} :shirabesleep: (recuerden actualizar sus tarjetas)'
    schedule_message(
        post_at=(today.replace(hour=9, minute=1, second=0)).strftime('%s'),
        text=text,
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
    schedule_message(
        post_at=(today.replace(hour=17, minute=50, second=0)).strftime('%s'),
        text='Recuerden actualizar sus tarjetas :rubyruntheotherway:',
        buttons=[{
            "text": "Link a Trello :trello:",
            "url": settings.URL_TRELLO,
        }],
        debug=True
    )
