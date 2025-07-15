# Standard Library
from datetime import datetime
import locale

# Third Party
from flask import Flask, request, Response, jsonify
import pytz
import requests
from slackeventsapi import SlackEventAdapter

# Reserbot
import settings
from bot_manager import BotManager
from team_manager import TeamManager

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
team = TeamManager()
reserbot = BotManager()


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')

@slack_event_adapter.on('message')
def message_event(data):
    event = data['event']
    message = event.get('text', '').lower()
    is_bot_message = event.get('bot_id') is not None

@app.route('/estudio', methods=['POST'])
def estudio():
    user = request.form.get('user_name')
    reserbot.post_message(
        text=f'@{user} va a tomar la hora de estudio :rubyhappy: anótate :bonk-doge:',
        buttons=[{
            'text': 'Ir al excel 📚',
            'url': settings.URL_EXCEL_LEARNING
        }],
    )
    return Response(), 200

@app.route('/lider-al-azar', methods=['POST'])
def lider_al_azar():
    user = request.form.get('user_name')
    today = datetime.now(pytz.timezone('America/Santiago'))
    random_leader = team.get_random_leader(today)
    if random_leader:
        reserbot.post_message(
            text=f'@{user} pidió un lider al azar: lidera {random_leader} :rubyrun:'
        )
    return Response(), 200

@app.route('/vacaciones', methods=['POST'])
def vacaciones():
    user = request.form.get('user_name')
    member_tag = request.form.get('text').strip()
    team.update_availability(member_tag, available=False)
    return Response(), 200

@app.route('/disponible', methods=['POST'])
def disponible():
    user = request.form.get('user_name')
    member_tag = request.form.get('text').strip()
    team.update_availability(member_tag, available=True)
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
