# Reserbot
import settings

# Third Party
import slack


class BotManager:

    channel = '#reservo-ti'

    def __init__(self):
        self.client = slack.WebClient(token=settings.BOT_TOKEN)
        # Use a debug channel for testing
        if settings.DEBUG:
            self.channel = '#reserbot-shhhh'

    def post_message(self, text, buttons=None):
        self.client.chat_postMessage(
            channel=self.channel,
            blocks=self.__build_message_blocks(text, buttons)
        )

    def schedule_message(self, post_at, text, buttons=None):
        self.client.chat_scheduleMessage(
            channel=self.channel,
            post_at=post_at,
            blocks=self.__build_message_blocks(text, buttons),
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