from datetime import datetime
import settings
import slack_client
import utils


lider_daily = utils.lider_daily()
if lider_daily:
    today = datetime.now()
    slack_client.schedule_text(
        channel=settings.CHANNEL_PROD,
        text=f'Hoy {today.strftime("%A %d")} lidera {lider_daily} :finoseñores:',
        post_at=(today.replace(hour=9, minute=35, second=0)).strftime('%s')
    )
    buttons = [
        {
            "text": "Daily :discord:",
            "url": settings.URL_DISCORD_DAILY,
        },
        {
            "text": "Tablero :trello:",
            "url": settings.URL_TRELLO,
        }
    ]
    slack_client.schedule_buttons(
        channel=settings.CHANNEL_PROD,
        buttons=buttons,
        post_at=(today.replace(hour=9, minute=50, second=0)).strftime('%s')
    )

