from settings import CHANNEL_PROD
import utils
import slack_client
from datetime import datetime


message_text = utils.lider_daily()
if message_text:
    now = datetime.now()
    slack_client.schedule_text(
        channel=CHANNEL_PROD, 
        text=message_text, 
        post_at=(now.replace(hour=9, minute=30, second=0)).strftime('%s')
    )
    slack_client.schedule_button(
        channel=CHANNEL_PROD, 
        btn_text='Link de la daily en WhereBy :ola2:', 
        post_at=(now.replace(hour=9, minute=55, second=0)).strftime('%s'), 
        url="https://whereby.com/reunion-tecnica-reservo"
    )
