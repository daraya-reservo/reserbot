# Standard library
from datetime import datetime
import locale

# Third Party
import pytz

# Reserbot
from bot_manager import BotManager
from team_manager import TeamManager
import utils


locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
today = datetime.now(pytz.timezone('America/Santiago'))
team = TeamManager()
reserbot = BotManager()

if utils.is_workday(today):
    # miembros del equipo no disponibles
    unavailable_members = team.get_unavailable_members(today)
    if unavailable_members:
        text = f'Hoy {today.strftime("%A")} no estará: {", ".join(unavailable_members)} :f2:'
        post_at = (today.replace(hour=9, minute=0, second=0)).strftime('%s')
        reserbot.schedule_message(
            post_at=post_at,
            text=text,
        )

    # integrante que lidera la daily hoy
    leader = team.get_daily_leader(today)
    text = f'Hoy {today.strftime("%A %d")} lidera {leader} :anime:'
    reserbot.schedule_message(
        post_at=(today.replace(hour=9, minute=1, second=0)).strftime('%s'),
        text=text,
        buttons=[
            {
                "text": "Abrir Trello :trello:",
                "url": 'https://trello.com/b/dZnTCMi3/tablero-desarrollo',
            },
            {
                "text": "Unirse a Meet :meet:",
                "url": 'https://meet.google.com/sft-muqe-ziq',
            },
        ],
    )

    # recordatorio de reuniones que ocurren hoy
    meetings = utils.get_meetings(today)
    for meeting in meetings:
        reserbot.schedule_message(
            post_at=(today.replace(hour=9, minute=45, second=0)).strftime('%s'),
            text=meeting['text'],
            buttons=[{
                'text': 'Unirse a la reunión :meet:',
                'url': meeting['url']
            }],
        )
