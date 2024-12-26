import settings
import slack


client = slack.WebClient(token=settings.BOT_TOKEN)

def publicar_mensaje(channel, text=None, buttons=None):
    blocks = _build_blocks(text=text, buttons=buttons)
    client.chat_postMessage(
        channel=channel,
        blocks=blocks
    )

def programar_mensaje(channel, post_at, text=None, buttons=None):
    blocks = _build_blocks(text=text, buttons=buttons)
    client.chat_scheduleMessage(
        channel=channel,
        post_at=post_at,
        blocks=blocks,
        text='mensaje programado',
    )

def _build_blocks(text=None, buttons=None):
    mensaje = []
    if text:
        mensaje.append({
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
        mensaje.append({
            'type': 'actions',
            'elements': btn_elements
        })
    return mensaje