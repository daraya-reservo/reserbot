from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter
from settings import SIGNING_SECRET, BOT_TOKEN
import slack
from random import choice
from schedule import lider_daily
from slack_client import post_text_message


app = Flask(__name__)
client = slack.WebClient(token=BOT_TOKEN)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')


def lider_aleatorio_daily(channel):
    team = ('Agustín', 'Dani', 'Hiho', 'Isi', 'Lucho', 'Manu', 'Nach', 'Pancho', 'Pato', 'Seba', 'Val')
    text = f"Hmmm que lidere {choice(team)} :shirabesleep:"
    post_text_message(channel, text)



@slack_event_adapter.on('message')
def message(payload):
    event = payload['event']
    if any([kw in event['text'] for kw in ('estudio', 'estudiar')]):
        client.chat_postMessage(
            channel=event['channel'],
            thread_ts=event['ts'],
            reply_broadcast=True,
            blocks = [{
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"<@{event['user']}> anótate en el excel :bonk-doge:"}
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
    					"url": 'https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit#gid=0'
    				}]
        		}]
        )
    elif event['text'] == 'random-daily':
        lider_aleatorio_daily(event['channel'])


@app.route('/random', methods=['POST'])
def random():
    lider_aleatorio_daily(f'#{request.form.get("channel_name")}')
    return Response(), 200


@app.route('/lider-daily', methods=['POST'])
def daily():
    '''
    client.chat_postMessage(
        channel=f'#{request.form.get("channel_name")}',
        blocks = [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": lider_daily() or "Hoy no toca daily"}
            },
        ]
    )
    '''
    post_text_message(f'#{request.form.get("channel_name")}', lider_daily() or "Hoy no toca daily")
    return Response(), 200


@app.route('/siguiente-daily', methods=['POST'])
def next():
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
