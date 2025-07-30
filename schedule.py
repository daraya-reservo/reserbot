# Reserbot
from bot_manager import BotManager
import links
import settings
from team_manager import TeamManager
import utils


today = utils.datetime_now()
team = TeamManager()
reserbot = BotManager(token=settings.BOT_TOKEN)

not_feriado = today.strftime('%Y-%m-%d') not in utils.feriados(today.year)
is_dia_habil = today.weekday() in range(5)  # [lunes a viernes]

if is_dia_habil and not_feriado:
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
                "url": links.url_trello,
            },
            {
                "text": "Unirse a Meet :meet:",
                "url": links.url_meet_daily,
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
