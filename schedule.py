# Standard library
from datetime import datetime
import locale

# Third Party
import pytz

# Reserbot
import settings
import slack_manager
from team_manager import TeamManager
import utils


locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
today = datetime.now(pytz.timezone('America/Santiago'))
team = TeamManager()

if utils.is_workday(today):
    # miembros del equipo no disponibles
    unavailable_members = {
        member['name']
        for member in team.members 
        if not member['is_available']
    }
    if today.weekday() == 4:  # viernes
        unavailable_members.add('Hiho')
    if unavailable_members:
        text = f'Hoy {today.strftime("%A")} no estará: {", ".join(unavailable_members)} :f2:'
        post_at = (today.replace(hour=9, minute=0, second=0)).strftime('%s')
        slack_manager.schedule_message(
            post_at=post_at,
            text=text,
        )

    # integrante que lidera la daily hoy
    leader = team.get_daily_leader(today)
    text = f'Hoy {today.strftime("%A %d")} lidera {leader} :anime:'
    slack_manager.schedule_message(
        post_at=(today.replace(hour=9, minute=1, second=0)).strftime('%s'),
        text=text,
        buttons=[
            {
                "text": "Abrir Trello :trello:",
                "url": settings.URL_TRELLO,
            },
            {
                "text": "Unirse a Meet :meet:",
                "url": settings.URL_MEET,
            },
        ],
    )

    # recordatorio de reuniones que ocurren hoy
    meetings = utils.get_meetings(today)
    minute = 45
    for meeting in meetings:
        slack_manager.schedule_message(
            post_at=(today.replace(hour=9, minute=minute, second=0)).strftime('%s'),
            text=meeting['text'],
            buttons=[{
                'text': 'Unirse a la reunión :meet:',
                'url': meeting['url']
            }],
        )
        minute += 1

