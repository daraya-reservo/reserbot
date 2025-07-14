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
import slack_manager
import team_manager
import utils

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')

@slack_event_adapter.on('message')
def message_event(data):
    event = data['event']
    message = event.get('text', '').lower()
    is_bot_message = event.get('bot_id') is not None
    message_estudio = 'estudio' in message and not is_bot_message
    if message_estudio:
        slack_manager.post_message(
            text=f'<@{event["user"]}> anótate en el excel :bonk-doge:',
            buttons=[{
                'text': 'Link al excel 📚',
                'url': settings.URL_EXCEL_LEARNING
            }],
        )

@app.route('/lider-al-azar', methods=['POST'])
def lider_al_azar():
    today = datetime.now(pytz.timezone('America/Santiago'))
    print(request.form)
    channel_id = request.form.get('channel_id')
    print(get_members(channel_id))
    print(team_manager.TeamManager(day=today).members)
    a = team_manager.TeamManager(day=today).get_random_leader()
    random_leader = utils.get_random_leader()
    if random_leader:
        slack_manager.post_message(
            text=f'Que lidere {random_leader} :rubyrun: {a}',
        )
    return Response(), 200

def get_members(channel_id):
    url = 'https://slack.com/api/conversations.members'
    headers = {'Authorization': f'Bearer {settings.BOT_TOKEN}'}
    params = {'channel': channel_id}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data.get('members', [])


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
