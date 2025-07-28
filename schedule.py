# Reserbot
from bot_manager import BotManager
from team_manager import TeamManager
import settings
import utils


today = utils.datetime_now()
team = TeamManager()
reserbot = BotManager(token=settings.BOT_TOKEN)

is_feriado = today.strftime('%Y-%m-%d') in utils.feriados()
is_dia_habil = today.weekday() in range(5)  # [lunes a viernes]

if not is_feriado and is_dia_habil:
    # miembros del equipo no disponibles
    unavailable_members = team.get_unavailable_members()
    if unavailable_members:
        reserbot.post(
            post_at=(today.replace(hour=9, minute=0, second=0)).strftime('%s'),
            text=f'Hoy {today.strftime("%A")} no estará: {", ".join(unavailable_members)} :f2:',
        )

    # miembro que lidera la daily hoy
    leader = team.get_daily_leader()
    reserbot.post(
        post_at=(today.replace(hour=9, minute=1, second=0)).strftime('%s'),
        text=f'Hoy {today.strftime("%A %d")} lidera {leader} :anime:',
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
        reserbot.post(
            post_at=(today.replace(hour=9, minute=45, second=0)).strftime('%s'),
            text=meeting['text'],
            buttons=[{
                'text': 'Unirse a la reunión :meet:',
                'url': meeting['url']
            }],
        )
