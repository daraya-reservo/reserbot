# Third Party
from flask import Flask, jsonify, request, Response

# Reserbot
import controllers


app = Flask(__name__)
controller = controllers.Controller()

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')

@app.route('/estudio', methods=['POST'])
def estudio():
    controller.post_message_estudio(request.form)
    return Response(), 200

@app.route('/lider-al-azar', methods=['POST'])
def lider_al_azar():
    controller.post_message_lider_al_azar(request.form)
    return Response(), 200

@app.route('/vacaciones', methods=['POST'])
def vacaciones():
    controller.update_member_availability(request.form, available=False)
    return Response(), 200

@app.route('/fin-vacaciones', methods=['POST'])
def fin_vacaciones():
    controller.update_member_availability(request.form, available=True)
    return Response(), 200

@app.route('/suscribir-rut', methods=['POST'])
def suscribir_rut():
    controller.suscribir_rut(request.form)
    return Response(), 200

@app.route('/desuscribir-rut', methods=['POST'])
def desuscribir_rut():
    controller.desuscribir_rut(request.form)
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

import settings
from slackeventsapi import SlackEventAdapter
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)
@slack_event_adapter.on('message')
def message_event(data):
    event = data['event']
    message = event.get('text', '').lower()
    is_bot_message = event.get('bot_id') is not None

"""
