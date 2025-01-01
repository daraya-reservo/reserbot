from settings import (
    BOT_TOKEN,
    DEBUG_ENV,
    PROD_ENV
)
import slack


client = slack.WebClient(token=BOT_TOKEN)

def publicar_mensaje(text=None, buttons=None, debug=True):
    channel = DEBUG_ENV if debug else PROD_ENV
    blocks = _build_blocks(text=text, buttons=buttons)
    client.chat_postMessage(
        channel=channel,
        blocks=blocks
    )

def programar_mensaje(post_at, text=None, buttons=None, debug=True):
    channel = DEBUG_ENV if debug else PROD_ENV
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