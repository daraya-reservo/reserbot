# Reserbot
import settings

# Third Party
import slack


client = slack.WebClient(token=settings.BOT_TOKEN)

def post_message(text=None, buttons=None):
    channel = (
        settings.QA_CHANNEL if settings.DEBUG 
        else settings.MAIN_CHANNEL
    )
    blocks = __build_message_blocks(text=text, buttons=buttons)
    client.chat_postMessage(
        channel=channel,
        blocks=blocks
    )

def schedule_message(post_at, text=None, buttons=None):
    channel = (
        settings.QA_CHANNEL if settings.DEBUG 
        else settings.MAIN_CHANNEL
    )
    blocks = __build_message_blocks(text=text, buttons=buttons)
    client.chat_scheduleMessage(
        channel=channel,
        post_at=post_at,
        blocks=blocks,
        text='scheduled message',
    )

def __build_message_blocks(text=None, buttons=None):
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


class BotManager:

    def __init__(self):
        self.client = slack.WebClient(token=settings.BOT_TOKEN)
        self.channel = settings.QA_CHANNEL if settings.DEBUG else settings.MAIN_CHANNEL

    def post_message(self, text=None, buttons=None):
        self.client.chat_postMessage(
            channel=self.channel,
            blocks=self.__build_message_blocks(text=text, buttons=buttons)
        )

    def schedule_message(self, post_at, text=None, buttons=None):
        self.client.chat_scheduleMessage(
            channel=self.channel,
            post_at=post_at,
            blocks=self.__build_message_blocks(text=text, buttons=buttons),
            text='scheduled message',
        )

    def __build_message_blocks(self, text=None, buttons=None):
        blocks = []
        if text:
            blocks.append({
                'type': 'section',
                'text': {'type': 'mrkdwn', 'text': text,},
            })
        if buttons:
            button_elements = [{
                'type': 'button',
                'text': {
                    'type': 'plain_text',
                    'text': button['text'],
                    'emoji': True
                },
                'style': 'primary',
                'url': button['url'],
            } for button in buttons]
            blocks.append({'type': 'actions', 'elements': button_elements})
        return blocks