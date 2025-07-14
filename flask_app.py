# Third Party
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from slackeventsapi import SlackEventAdapter

# Reserbot
import settings
import slack_manager
import team_manager
import utils

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="darayadcc",
    password="mysqladmin",
    hostname="darayadcc.mysql.pythonanywhere-services.com",
    databasename="darayadcc$reserbot",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class TeamMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))
    tag = db.Column(db.String(4096))
    dailies = db.Column(db.Integer)
    is_available = db.Column(db.Boolean)


slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)


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
    print(request.form)
    channel_id = request.form.get('channel_id')
    print(get_members(channel_id))

    random_leader = utils.get_random_leader()
    if random_leader:
        slack_manager.post_message(
            text=f'Que lidere {random_leader} :rubyrun:',
            debug=True
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
