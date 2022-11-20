from settings import XLSX_FILE, TIME_ZONE, BOT_TOKEN
import slack
import locale
from datetime import datetime, timedelta


client = slack.WebClient(token=BOT_TOKEN)
bot_id = client.api_call('auth.test')['user_id']

def get_daily_leader():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # para setear el lenguaje en el server
    weekday = datetime.now(TIME_ZONE)
    leader = XLSX_FILE[XLSX_FILE['Día'] == weekday.strftime('%Y-%m-%d')]['Responsable'].values
    return (f"Daily de hoy {weekday.strftime('%A %d')} la lidera {leader[0]} :finoseñores:" 
        if leader.size
        else None)  

def next_daily():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # para setear el lenguaje en el server
    weekday = datetime.now(TIME_ZONE) + timedelta(days=1)
    leader = XLSX_FILE[XLSX_FILE['Día'] == weekday.strftime('%Y-%m-%d')]['Responsable'].values
    return (f"Daily de mañana {weekday.strftime('%A %d')} la lidera {leader[0]} :shirabesleep:" 
        if leader.size
        else None)  

def slack_simple_message(channel, message):
    client.chat_postMessage(channel=channel, text=message)

def slack_button_message(channel, message, button_text, link):
    client.chat_postMessage(
            channel=channel,
            blocks = [{
                "type": "section",
                "text": {
                    "type": "mrkdwn", "text": message
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text", "text": button_text, "emoji": True
                    },
                    "style": "primary",
                    "value": "whereby",
                    "url": link,
                    "action_id": "button-action"
                }
            }]
        )

 