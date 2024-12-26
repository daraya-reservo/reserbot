from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter
import settings
from bot_interface import publicar_mensaje
import utils

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')

@slack_event_adapter.on('message')
def message_event(data):
    event = data['event']
    mensaje = event.get('text', '').lower()
    channel = settings.CHANNEL_TESTING # event['channel']
    mensaje_estudio = 'estudio' in mensaje and event.get('bot_id') is None
    if mensaje_estudio:
        publicar_mensaje(
            channel=channel,
            text=f'<@{event["user"]}> anótate en el excel :bonk-doge:',
            buttons=[{
                'text': 'Link al excel 📚',
                'url': settings.URL_ESTUDIO
            }]
        )

@app.route('/lider-al-azar', methods=['POST'])
def lider_al_azar():
    lider = utils.get_lider_al_azar()
    publicar_mensaje(
        channel=settings.CHANNEL_TESTING,  # f'#{request.form.get("channel_name")}',
        text=f'Que lidere {lider} :rubyrun:'
    )
    return Response(), 200

@app.route('/lider-daily-hoy', methods=['POST'])
def lider_daily_hoy():
    if request.form['user_name'] == 'daraya':
        lider = request.form['text']
        utils.update_dailies_equipo(lider)
        publicar_mensaje(
            channel=settings.CHANNEL_TESTING,
            text=f'Hoy lideró {lider}'
        )
    return Response(), 200

@app.route('/vacaciones', methods=['POST'])
def vacaciones():
    if request.form['user_name'] == 'daraya':
        integrante = request.form['text']
        utils.update_vacaciones(integrante)
        publicar_mensaje(
            channel=settings.CHANNEL_TESTING,
            text=f'{integrante} se tomará unos días'
        )
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
