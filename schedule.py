from settings import BOT_TOKEN, XLSX_FILE, CHANNEL_PROD, CHANNEL_DEV
import slack
import locale
from datetime import datetime


client = slack.WebClient(token=BOT_TOKEN)
now = datetime.now()


def lider_daily():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # para setear el lenguaje en el server
    lider_daily = XLSX_FILE[XLSX_FILE['Día'] == now.strftime('%Y-%m-%d')]['Responsable'].values
    return f"Daily de hoy {now.strftime('%A %d')} la lidera {lider_daily[0]} :finoseñores:" if lider_daily.size else None


message_text = lider_daily()
if message_text:
    client.chat_scheduleMessage(
        channel=CHANNEL_PROD,
        post_at=(now.replace(hour=9, minute=30, second=0)).strftime('%s'),
        text='mensaje daily',
        blocks = [{
            "type": "section",
            "text": {"type": "mrkdwn", "text": message_text},
        }]
    )
    client.chat_scheduleMessage(
        channel=CHANNEL_PROD,
        post_at=(now.replace(hour=9, minute=55, second=0)).strftime('%s'),
        text='boton daily',
        blocks = [{
			"type": "actions",
			"elements": [{
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Link de la daily en WhereBy :ola2:",
					"emoji": True
				},
				"style": "primary",
				"url": "https://whereby.com/reunion-tecnica-reservo",
			}]
		}]
    )
