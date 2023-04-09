from flask import Flask, request, Response, jsonify
import openai
from slackeventsapi import SlackEventAdapter
import settings
import slack_client
import utils


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)
openai.api_key = settings.API_KEY


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')

@slack_event_adapter.on('message')
def message_event(payload):
    event = payload['event']
    if event['text'].startswith('chatgpt:'):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=event['text'].split('chatgpt:')[1],
            max_tokens=250,
            temperature=0,
            n=1,
        )
        chatgpt_text = response.choices[0].text
        slack_client.post_text(
            channel=event['channel'],
            text=chatgpt_text,
        )
    elif any([kw in event['text'].lower() for kw in ('estudio', 'estudiar')]) and not event.get('bot_id'):
        slack_client.post_reply(
            channel=event['channel'],
            text=f'<@{event["user"]}> anótate en el excel :bonk-doge:',
            btn_text='Link al excel de estudio 📚',
            url='https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit#gid=0'
        )
    elif event['text'] == 'lider-random':
        slack_client.post_text(
            channel=event['channel'],
            text=utils.lider_random()
        )
    elif event['text'] == 'lider-siguiente':
        slack_client.post_text(
            channel=event['channel'],
            text=utils.lider_siguiente()
        )
    elif event['text'] == 'reserbot-debugger':
        pass

@app.route('/lider-random', methods=['POST'])
def lider_random():
    slack_client.post_text(
        channel=f'#{request.form.get("channel_name")}',
        text=utils.lider_random()
    )
    return Response(), 200

@app.route('/lider-daily', methods=['POST'])
def lider_daily():
    slack_client.post_text(
        channel=f'#{request.form.get("channel_name")}',
        text=utils.lider_daily() or "Hoy no toca daily :shirabesleep:"
    )
    return Response(), 200

@app.route('/lider-siguiente', methods=['POST'])
def lider_siguiente():
    slack_client.post_text(
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
