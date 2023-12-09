from flask import Flask, request, Response, jsonify
import random
from slackeventsapi import SlackEventAdapter
import settings
import slack_client


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')

@slack_event_adapter.on('message')
def message_event(payload):
    event = payload['event']
    message = event.get('text', '')
    if 'estudio' in message.lower() and event.get('bot_id') is None:
        slack_client.post_message(
            channel=event['channel'],
            text=f'<@{event["user"]}> anótate en el excel :bonk-doge:',
            btn_text='Link al excel de estudio 📚',
            url=settings.URL_EXCEL_ESTUDIO
        )
    elif message == 'lider-random':
        slack_client.post_message(
            channel=event['channel'],
            text=f'Que lidere {random.choice([member[0] for member in settings.TEAM])} :rubyrun:'
        )

@app.route('/lider-random', methods=['POST'])
def lider_random():
    slack_client.post_message(
        channel=f'#{request.form.get("channel_name")}',
        text=f'Que lidere {random.choice([member[0] for member in settings.TEAM])} :rubyrun:'
    )
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
