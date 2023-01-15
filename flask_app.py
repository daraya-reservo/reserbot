from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter
from settings import SIGNING_SECRET
import slack_client
import utils


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')


@slack_event_adapter.on('message')
def message(payload):
    event = payload['event']
    if any([kw in event['text'] for kw in ('estudio', 'estudiar')]):
        slack_client.post_reply_message(
            channel=event['channel'],
            ts=event['ts'],
            text=f'<@{event["user"]}> anótate en el excel :bonk-doge:',
            btn_text='Link del excel de estudio 📚',
            url='https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit#gid=0'
        )
    elif event['text'] == 'lider-aleatorio':
        slack_client.post_text_message(
            channel=event['channel'],
            text=utils.lider_aleatorio()
        )
    elif event['text'] == 'lider-siguiente':
        slack_client.post_text_message(
            channel=event['channel'],
            text=utils.lider_siguiente()
        )


@app.route('/lider-aleatorio', methods=['POST'])
def lider_aleatorio():
    slack_client.post_text_message(
        channel=f'#{request.form.get("channel_name")}',
        text=utils.lider_aleatorio()
    )
    return Response(), 200


@app.route('/lider-daily', methods=['POST'])
def daily():
    slack_client.post_text_message(
        channel=f'#{request.form.get("channel_name")}',
        text=utils.lider_daily() or "Hoy no toca daily :shirabesleep:"
    )
    return Response(), 200


@app.route('/lider-siguiente', methods=['POST'])
def lider_siguiente():
    slack_client.post_text_message(
        channel=f'#{request.form.get("channel_name")}',
        text=utils.lider_siguiente()
    )
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
