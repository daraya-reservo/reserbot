from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter
import settings
import slack_client
import utils


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')

@slack_event_adapter.on('message')
def message_event(data):
    event = data['event']
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
            text=f'Que lidere {utils.get_random_teammate()} :rubyrun:'
        )
    elif message == 'get-daily-leader':
        slack_client.post_message(
            channel=event['channel'],
            text='el lider sera ' + utils.get_daily_leader()
        )
    elif message == 'get-newsletter':
        slack_client.post_message(
            channel=event['channel'],
            btn_text='Leer newsletter',
            url=settings.URL_NOTION_NEWSLETTERS
        )

@app.route('/lider-random', methods=['POST'])
def lider_random():
    slack_client.post_message(
        channel=f'#{request.form.get("channel_name")}',
        text=f'Que lidere {utils.get_random_teammate()} :rubyrun:'
    )
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
