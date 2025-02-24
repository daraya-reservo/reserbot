# Reserbot
import settings

# Third Party
import slack


client = slack.WebClient(token=settings.BOT_TOKEN)

def post_message(text=None, buttons=None, debug=False):
    channel = (
        settings.DEBUG_ENV if debug 
        else settings.PROD_ENV
    )
    blocks = _build_message_blocks(text=text, buttons=buttons)
    client.chat_postMessage(
        channel=channel,
        blocks=blocks
    )

def schedule_message(post_at, text=None, buttons=None, debug=False):
    channel = (
        settings.DEBUG_ENV if debug 
        else settings.PROD_ENV
    )
    blocks = _build_message_blocks(text=text, buttons=buttons)
    client.chat_scheduleMessage(
        channel=channel,
        post_at=post_at,
        blocks=blocks,
        text='scheduled message',
    )

def _build_message_blocks(text=None, buttons=None):
    blocks = []
    if text:
        blocks.append({
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
        blocks.append({
            'type': 'actions',
            'elements': btn_elements
        })
    return blocks