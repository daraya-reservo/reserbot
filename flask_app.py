# Third Party
from flask import Flask, request, Response, jsonify
from slackeventsapi import SlackEventAdapter

# Reserbot
import settings
import slack_manager
import team_manager
import utils

app = Flask(__name__)
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
    # if message_estudio:
    #     slack_manager.post_message(
    #         text=f'<@{event["user"]}> anótate en el excel :bonk-doge:',
    #         buttons=[{
    #             'text': 'Link al excel 📚',
    #             'url': settings.URL_EXCEL_LEARNING
    #         }],
    #     )

@app.route('/lider-al-azar', methods=['POST'])
def lider_al_azar():
    random_leader = utils.get_random_leader()
    if random_leader:
        slack_manager.post_message(
            text=f'Que lidere {random_leader} :rubyrun:',
            debug=True
        )
    return Response(), 200

@app.route('/actualizar-dailies', methods=['POST'])
def actualizar_dailies():
    if request.form['user_name'] == 'daraya':
        member_tag = request.form['text']
        team_manager.update_dailies(member_tag)
    return Response(), 200

@app.route('/actualizar-disponibilidad', methods=['POST'])
def actualizar_disponibilidad():
    if request.form['user_name'] == 'daraya':
        member_tag = request.form['text']
        team_manager.update_disponibilidad(member_tag)
    return Response(), 200


if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
