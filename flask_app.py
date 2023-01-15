from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter
from settings import SIGNING_SECRET, BOT_TOKEN
import slack
from random import choice
from schedule import lider_daily
from slack_client import post_text_message, post_reply_message
from utils import lider_aleatorio_daily


app = Flask(__name__)
client = slack.WebClient(token=BOT_TOKEN)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')


@slack_event_adapter.on('message')
def message(payload):
    event = payload['event']
    message_text = event.get('text')
    if any([kw in message_text for kw in ('estudio', 'estudiar')]):
        post_reply_message(
            channel=event['channel'], 
            ts=event['ts'], 
            text=f'<@{event["user"]}> anótate en el excel :bonk-doge:', 
            btn_text='Link del excel de estudio 📚', 
            url='https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit#gid=0'
        )
    elif message_text == 'lider-aleatorio':
        post_text_message(
            channel=event['channel'], 
            text=lider_aleatorio_daily()
        )


@app.route('/lider-aleatorio', methods=['POST'])
def daily_aleatorio():
    post_text_message(
        channel=f'#{request.form.get("channel_name")}', 
        text=lider_aleatorio_daily()
    )
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
