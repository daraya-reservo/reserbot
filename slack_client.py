import settings
import slack


client = slack.WebClient(token=settings.BOT_TOKEN)


def post_text(channel, text):
    client.chat_postMessage(
        channel=channel,
        blocks=[{'type': 'section', 'text': {'type': 'mrkdwn','text': text}}]
    )


def post_reply(channel, ts, text, btn_text, url):
    client.chat_postMessage(
        channel=channel,
        thread_ts=ts,
        reply_broadcast=True,
        blocks = [
            {
                'type': 'section',
                'text': {'type': 'mrkdwn', 'text': text}
            },
            {
                'type': 'actions',
                'elements': [{
                    'type': 'button',
                    'text': {'type': 'plain_text', 'text': btn_text, 'emoji': True},
                    'style': 'primary',
                    'url': url
                }]
            }
        ]
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

def schedule_button(channel, text, post_at, url):
    client.chat_scheduleMessage(
        channel=channel,
        post_at=post_at,
        text='botón programado',
        blocks = [{
			"type": "actions",
			"elements": [{
				"type": "button",
				"text": {"type": "plain_text", "text": text, "emoji": True},
				"style": "primary",
				"url": url,
			}]
		}]
    )
