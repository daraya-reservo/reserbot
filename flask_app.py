from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter
from settings import SIGNING_SECRET, BOT_TOKEN
import slack


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)
client = slack.WebClient(token=BOT_TOKEN)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo. Wenas!')

@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))


@slack_event_adapter.on('message')
def message_estudio(payload):
    estudio_keywords = ['estudio', 'estudiar']
    event = payload.get('event', {})
    user_id = event.get('user')
    if any([kw in event.get('text', '') for kw in estudio_keywords]):
        client.chat_postMessage(
            channel=event['channel'],
            thread_ts=event['ts'],
            reply_broadcast=True,
            blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn", "text": f'<@{user_id}> anótate en el excel :bonk-doge:'
                    },
                },
                {
        			"type": "actions",
        			"elements": [{
        					"type": "button",
        					"text": {
        						"type": "plain_text",
        						"text": 'Link del excel de estudio 📚',
        						"emoji": True
        					},
        					"style": "primary",
        					"url": 'https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit#gid=0',
        					"value": "whereby",
        					"action_id": "button-action"
    				}]
        		}
            ]
        )


if __name__ == '__main__':
    app.run(port=5000)




"""
@app.route('/daily', methods=['POST'])
def daily():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # para setear el lenguaje en el server
    weekday = datetime.now()
    leader = XLSX_FILE[XLSX_FILE['Día'] == weekday.strftime('%Y-%m-%d')]['Responsable'].values
    button_text = 'Click aquí pa ir a WhereBy :ola2:'
    text = f"Daily de hoy {weekday.strftime('%A %d')} la lidera {leader[0]} :finoseñores:" if leader.size else None

    client.chat_postMessage(
        channel=f'#{request.form.get('channel_name')}',
        text=text if text else 'Hoy no hay daily'
    )
    return Response(), 200
"""
