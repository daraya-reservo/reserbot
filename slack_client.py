import settings
import slack


client = slack.WebClient(token=settings.BOT_TOKEN)

def post_message(channel, text, btn_text=None, url=None):
    blocks = [
        {
            'type': 'section',
            'text': {'type': 'mrkdwn', 'text': text}
        }
    ]
    if btn_text:
        blocks.append({
            'type': 'actions',
            'elements': [{
                'type': 'button',
                'text': {
                    'type': 'plain_text',
                    'text': btn_text,
                    'emoji': True
                },
                'style': 'primary',
                'url': url
            }]
        })
    client.chat_postMessage(
        channel=channel,
        blocks=blocks
    )


def schedule_message(channel, post_at, text=None, buttons=None):
    blocks = []
    if text:
        blocks.append({
            'type': 'section',
            'text': {'type': 'mrkdwn', 'text': text}
        })
    if buttons:
        elements = [{
            'type': 'button',
            'text': {'type': 'plain_text', 'text': button['text']},
            'style': 'primary',
            'url': button['url']
        } for button in buttons]
        blocks.append({
            'type': 'actions',
            'elements': elements,
        })
    client.chat_scheduleMessage(
        channel=channel,
        post_at=post_at,
        text='mensaje programado',
        blocks=blocks
    )









