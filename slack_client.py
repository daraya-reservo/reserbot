import settings
import slack
from utils import build_message


client = slack.WebClient(token=settings.BOT_TOKEN)

def post_message(channel, text=None, buttons=None):
    blocks = build_message(text=text, buttons=buttons)
    client.chat_postMessage(
        channel=channel,
        blocks=blocks
    )

def schedule_message(channel, post_at, text=None, buttons=None):
    blocks = build_message(text=text, buttons=buttons)
    client.chat_scheduleMessage(
        channel=channel,
        post_at=post_at,
        blocks=blocks,
        text='mensaje programado',
    )
