from settings import XLSX_FILE, TIME_ZONE, BOT_TOKEN
import slack
import locale
from datetime import datetime, timedelta
from utils import slack_simple_message, get_daily_leader, slack_button_message

print("======================================")
print(datetime.now())
print(datetime.now(TIME_ZONE))
print("======================================")

"""
slack_simple_message(channel='#reserbot-shhhh', message='a '+ get_daily_leader())
client = slack.WebClient(token=BOT_TOKEN)

weekday = datetime.now(TIME_ZONE)
leader = XLSX_FILE[XLSX_FILE['Día'] == weekday.strftime('%Y-%m-%d')]['Responsable'].values
message = (f"Daily de hoy {weekday.strftime('%A %d')} la lidera {leader[0]} :finoseñores:"
            if leader.size
            else None)
client.chat_postMessage(channel="#reserbot-shhhh", text=message)
"""