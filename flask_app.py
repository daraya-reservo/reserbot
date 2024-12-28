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
    channel = settings.TEST_ENV # event['channel']
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
    lider_al_azar = utils.get_lider_al_azar()
    if lider_al_azar:
        publicar_mensaje(
            channel=settings.TEST_ENV,  # f'#{request.form.get("channel_name")}',
            text=f'Que lidere {lider_al_azar["nombre"]} :rubyrun:'
        )
    return Response(), 200

@app.route('/actualizar-dailies', methods=['POST'])
def actualizar_dailies():
    if request.form['user_name'] == 'daraya':
        integrante = request.form['text']
        utils.update_dailies(integrante)
        publicar_mensaje(
            channel=settings.TEST_ENV,
            text=f'Hoy lideró {integrante}'
        )
    print('integrantes actualizados')
    print(utils.get_integrantes_equipo())
    return Response(), 200

@app.route('/actualizar-disponibilidad', methods=['POST'])
def actualizar_disponibilidad():
    if request.form['user_name'] == 'daraya':
        integrante_tag = request.form['text']
        integrante_actualizado = utils.update_disponibilidad(integrante_tag)
        if not integrante_actualizado['disponible']:
            publicar_mensaje(
                channel=settings.TEST_ENV,
                text=f'{integrante_actualizado["nombre"]} se tomará unos días :rubyrun:'
            )
        print('integrantes actualizados')
        print(utils.get_integrantes_equipo())
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
