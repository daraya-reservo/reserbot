from datetime import datetime
import settings
import slack_client
import utils


message_lider_daily = utils.lider_daily()
if message_lider_daily:
    now = datetime.now()
    slack_client.schedule_text(
        channel=settings.CHANNEL_PROD,
        text=message_lider_daily,
        post_at=(now.replace(hour=9, minute=30, second=0)).strftime('%s')
    )
    slack_client.schedule_button(
        channel=settings.CHANNEL_PROD,
        text='Ir al Sirius Bisnes (Discord) :ola2:',
        post_at=(now.replace(hour=9, minute=55, second=0)).strftime('%s'),
        url="https://discord.com/channels/897964285559472158/1014947999010533416"
    )

