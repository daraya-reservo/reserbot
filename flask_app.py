from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter
import settings
import slack_client
import utils

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)
integrantes_equipo = [integrante['nombre'] for integrante in utils.get_integrantes_equipo()]


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')

@slack_event_adapter.on('message')
def message_event(data):
    event = data['event']
    message = event.get('text', '').lower()
    channel = settings.CHANNEL_TESTING # event['channel']
    if 'estudio' in message and event.get('bot_id') is None:
        slack_client.post_message(
            channel=channel,
            text=f'<@{event["user"]}> anótate en el excel :bonk-doge:',
            buttons=[{
                'text': 'Link al excel 📚',
                'url': settings.URL_ESTUDIO
            }]
        )

@app.route('/lider-random', methods=['POST'])
def lider_random():
    global integrantes_equipo
    if integrantes_equipo:
        lider, integrantes_equipo = utils.get_lider_random(integrantes_equipo)
        slack_client.post_message(
            channel=settings.CHANNEL_TESTING,  # f'#{request.form.get("channel_name")}',
            text=f'Que lidere {lider} :rubyrun:'
        )
    return Response(), 200

@app.route('/lider-daily-hoy', methods=['POST'])
def lider_daily_hoy():
    if request.form.get('user_name') == 'daraya':
        print('request.form')
        print(request.form)
        slack_client.post_message(
            channel=settings.CHANNEL_TESTING,  # f'#{request.form.get("channel_name")}',
            text='<@daraya>'
        )
    return Response(), 200

@app.route('/lider-daily', methods=['POST'])
def lider_daily():
    slack_client.post_message(
        channel=settings.CHANNEL_TESTING,  # f'#{request.form.get("channel_name")}',
        text=utils.get_lider_daily()
    )
    return Response(), 200

@app.route('/vacaciones', methods=['POST'])
def lider_daily():
    slack_client.post_message(
        channel=settings.CHANNEL_TESTING,  # f'#{request.form.get("channel_name")}',
        text=utils.get_lider_daily()
    )
    return Response(), 200



if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
