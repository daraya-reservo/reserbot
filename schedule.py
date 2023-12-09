from datetime import datetime
import settings
import slack_client
import utils


lider_daily = utils.lider_daily()
if lider_daily:
    today = datetime.now()
    slack_client.schedule_message(
        channel=settings.CHANNEL_PROD,
        post_at=(today.replace(hour=9, minute=35, second=0)).strftime('%s'),
        text=f'Hoy {today.strftime("%A %d")} lidera {lider_daily} :finoseñores:',
    )
    buttons = [
        {
            "text": "Daily :discord2:",
            "url": settings.URL_DISCORD_DAILY,
        },
        {
            "text": "Abrir Tablero :trello:",
            "url": settings.URL_TRELLO,
        }
    ]
    slack_client.schedule_message(
        channel=settings.CHANNEL_PROD,
        post_at=(today.replace(hour=9, minute=50, second=0)).strftime('%s'),
        buttons=buttons,
    )

