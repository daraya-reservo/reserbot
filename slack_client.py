import settings
import slack


client = slack.WebClient(token=settings.BOT_TOKEN)

def post_text(channel, text):
    client.chat_postMessage(
        channel=channel,
        blocks=[
            {
                'type': 'section', 
                'text': {'type': 'mrkdwn','text': text}
            }
        ]
    )

def post_reply(channel, text, btn_text, url):
    client.chat_postMessage(
        channel=channel,
        blocks = [
            {
                'type': 'section',
                'text': {'type': 'mrkdwn', 'text': text}
            },
            {
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
            }
        ]
    )

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
    client.chatPostMessage(
        channel=channel,
        blocks=blocks
    )

def schedule_text(channel, text, post_at):
    client.chat_scheduleMessage(
        channel=channel,
        post_at=post_at,
        text='texto programado',
        blocks = [{
            "type": "section",
            "text": {"type": "mrkdwn", "text": text},
        }]
    )

def schedule_buttons(channel, buttons, post_at):
    elements = []
    for button in buttons:
        elements.append({
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": button["text"]
            },
            "style": "primary",
            "url": button["url"]
        })
    client.chat_scheduleMessage(
        channel=channel,
        post_at=post_at,
        text='botones programados',
        blocks = [
            {
                "type": "divider"
            },
            {
                "type": "actions",
                "elements": elements
            },
		]
    )









