from settings import BOT_TOKEN, XLSX_FILE, CHANNEL_PROD, CHANNEL_DEV
import slack
import locale
from datetime import datetime


client = slack.WebClient(token=BOT_TOKEN)

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # para setear el lenguaje en el server
now = datetime.now()
lider_daily = XLSX_FILE[XLSX_FILE['Día'] == now.strftime('%Y-%m-%d')]['Responsable'].values
button_text = 'Link de la daily en WhereBy :ola2:'
url_daily = 'https://whereby.com/reunion-tecnica-reservo'
message_text = f"Daily de hoy {now.strftime('%A %d')} la lidera {lider_daily[0]} :finoseñores:" if lider_daily.size else None

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
					"text": button_text,
					"emoji": True
				},
				"style": "primary",
				"url": url_daily,
			}]
		}]
    )

