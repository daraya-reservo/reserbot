from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter
import settings
import bot
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
    mensaje_estudio = 'estudio' in mensaje and event.get('bot_id') is None
    if mensaje_estudio:
        bot.publicar_mensaje(
            text=f'<@{event["user"]}> anótate en el excel :bonk-doge:',
            buttons=[{
                'text': 'Link al excel 📚',
                'url': settings.URL_ESTUDIO
            }],
            debug=True
        )

@app.route('/lider-al-azar', methods=['POST'])
def lider_al_azar():
    lider_al_azar = utils.get_lider_al_azar()
    if lider_al_azar:
        bot.publicar_mensaje(
            text=f'Que lidere {lider_al_azar} :rubyrun:',
            debug=True
        )
    return Response(), 200

@app.route('/actualizar-dailies', methods=['POST'])
def actualizar_dailies():
    if request.form['user_name'] == 'daraya':
        integrante_tag = request.form['text']
        utils.update_dailies(integrante_tag)
    return Response(), 200

@app.route('/actualizar-disponibilidad', methods=['POST'])
def actualizar_disponibilidad():
    if request.form['user_name'] == 'daraya':
        integrante_tag = request.form['text']
        utils.update_disponibilidad(integrante_tag)
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
