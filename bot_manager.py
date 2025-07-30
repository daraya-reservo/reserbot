# Third Party
import slack


class BotManager:

    def __init__(self, token):
        self.client = slack.WebClient(token=token)
        self.channel = '#reservo-ti'

    def post(self, text, buttons=None, post_at=None, production=True):
        prepared_message = {
            'channel': self.channel if production else '#reserbot-shhhh',
            'blocks': self.__build_message_blocks(text, buttons),
        }
        if post_at:
            prepared_message['post_at'] = post_at
            prepared_message['text'] = 'scheduled message'
            self.client.chat_scheduleMessage(**prepared_message)
        else:
            self.client.chat_postMessage(**prepared_message)

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
                'style': button.get('style', 'primary'),
                'url': button['url'],
            } for button in buttons]
            blocks.append({'type': 'actions', 'elements': button_elements})
        return blocks
