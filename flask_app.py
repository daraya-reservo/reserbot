# Third Party
from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter

# Reserbot
import settings
from slack_manager import post_message
from team_manager import (
    update_dailies,
    update_disponibilidad,
)
from utils import get_random_leader

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')

@slack_event_adapter.on('message')
def message_event(data):
    event = data['event']
    message = event.get('text', '').lower()
    message_estudio = 'estudio' in message and not event.get('bot_id')
    if message_estudio:
        post_message(
            text=f'<@{event["user"]}> anótate en el excel :bonk-doge:',
            buttons=[{
                'text': 'Link al excel 📚',
                'url': settings.URL_EXCEL_LEARNING
            }],
        )

@app.route('/lider-al-azar', methods=['POST'])
def lider_al_azar():
    random_leader = get_random_leader()
    if random_leader:
        post_message(text=f'Que lidere {random_leader} :rubyrun:')
    return Response(), 200

@app.route('/actualizar-dailies', methods=['POST'])
def actualizar_dailies():
    if request.form['user_name'] == 'daraya':
        member_tag = request.form['text']
        update_dailies(member_tag)
    return Response(), 200

@app.route('/actualizar-disponibilidad', methods=['POST'])
def actualizar_disponibilidad():
    if request.form['user_name'] == 'daraya':
        member_tag = request.form['text']
        update_disponibilidad(member_tag)
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
