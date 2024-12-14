from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter
import settings
import slack_client
import utils

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)
team_members = list(utils.get_team().keys())


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
    global team_members
    if team_members:
        lider_random, team_members = utils.get_lider_random(team_members)
        slack_client.post_message(
            channel=settings.CHANNEL_TESTING,  # f'#{request.form.get("channel_name")}',
            text=f'Que lidere {lider_random} :rubyrun:'
        )
    return Response(), 200

@app.route('/lider-daily-hoy', methods=['POST'])
def lider_daily_hoy():
    if request.form.get('user_name') == 'daraya':
        slack_client.post_message(
            channel=settings.CHANNEL_TESTING,  # f'#{request.form.get("channel_name")}',
            text='jkhjkh'
        )
    print(request.form)
    print(request.form.get('channel_name'))
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
