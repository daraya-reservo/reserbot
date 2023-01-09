import slack
from settings import BOT_TOKEN


client = slack.WebClient(token=BOT_TOKEN)


def post_text_message(channel, text):
    client.chat_postMessage(
        channel=channel,
        blocks=[{
            'type': 'section',
            'text': {'type': 'mrkdwn','text': text}
        }]
    )


def post_reply_message(channel, ts, text, btn_text, url):
    client.chat_postMessage(
        channel=channel,
        thread_ts=ts,
        reply_broadcast=True,
        blocks = [{
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
            }]
    )