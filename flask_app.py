from flask import Flask, request, Response, jsonify
from utils import slack_simple_message, get_daily_leader, slack_button_message, bot_id, next_daily
from slackeventsapi import SlackEventAdapter
from settings import SIGNING_SECRET, BOT_TOKEN
import slack


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)
client = slack.WebClient(token=BOT_TOKEN)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo. Wenas!')

@app.route('/daily', methods=['POST'])
def daily():
    channel = request.form.get('channel_name')
    msg = get_daily_leader()
    slack_simple_message(
        channel=f'#{channel}',
        message=msg if msg else 'Hoy no hay daily'
    )
    return Response(), 200


@app.route('/next', methods=['POST'])
def siguiente_daily():
    channel = request.form.get('channel_name')
    msg = next_daily()
    slack_simple_message(
        channel=f'#{channel}',
        message=msg if msg else 'Hoy no hay daily'
    )
    return Response(), 200


@app.route('/slack/events', methods=['POST'])
def slack_event():
    print('request:', request.get_json())
    challenge = request.get_json().get('challenge', '')
    return jsonify(challenge=challenge)


@slack_event_adapter.on('message')
def message_estudio(payload):
    keywords = ['estudio', 'estudiar']
    event = payload.get('event', {})
    channel_id = event.get('channel')
    channel_name = client.conversations_info(channel=channel_id)['channel']['name']
    user_id = event.get('user')
    text = event.get('text')
    message = f'<@{user_id}> anótate en el excel :abogato: ->'
    link = 'https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit#gid=0'
    if bot_id != user_id and channel_name == 'reserbot-shhhh' and any([kw in text for kw in keywords]):
        slack_button_message(
            channel=channel_id,
            message=message,
            button_text='Link al excel de estudio',
            link=link
        )


if __name__ == '__main__':
    app.run(port=5000)