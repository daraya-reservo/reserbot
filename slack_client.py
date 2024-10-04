import settings
import slack


client = slack.WebClient(token=settings.BOT_TOKEN)

def prepare_message(text=None, buttons=None):
    message = []
    if text:
        message.append({
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': text
            }
        })
    if buttons:
        btn_elements = [{
            'type': 'button',
            'text': {
                'type': 'plain_text',
                'text': button['text'],
                'emoji': True
            },
            'style': 'primary',
            'url': button['url']
        } for button in buttons]
        message.append({
            'type': 'actions',
            'elements': btn_elements
        })
    return message

def post_message(channel, text=None, buttons=None):
    blocks = prepare_message(text=text, buttons=buttons)
    client.chat_postMessage(
        channel=channel,
        blocks=blocks
    )

def schedule_message(channel, post_at, text=None, buttons=None):
    blocks = prepare_message(text=text, buttons=buttons)
    client.chat_scheduleMessage(
        channel=channel,
        post_at=post_at,
        blocks=blocks,
        text='mensaje programado',
    )
