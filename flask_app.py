# Third Party
from flask import (
    Flask,
    jsonify,
    request,
    Response,
)

# Reserbot
import bot_manager
import links
import team_manager


app = Flask(__name__)
team = team_manager.TeamManager()
bot = bot_manager.BotManager()


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(message='Bot de Reservo')

@app.route('/estudio', methods=['POST'])
def estudio():
    user = request.form.get('user_name')
    bot.post(
        channel=f"#{request.form.get('channel_name')}",
        text=f'@{user} va a tomar la hora de estudio :rubyhappy: anótate :bonk-doge:',
        buttons=[{
            'text': 'Ir al excel 📚',
            'url': links.url_excel_estudio
        }],
    )
    return Response(), 200

@app.route('/lider-al-azar', methods=['POST'])
def lider_al_azar():
    user = request.form.get('user_name')
    random_leader = team.get_random_daily_leader()
    if random_leader:
        bot.post(
            channel=f"#{request.form.get('channel_name')}",
            text=f'@{user} pidió un lider al azar: lidera {random_leader} :rubyrun:'
        )
    return Response(), 200

@app.route('/vacaciones', methods=['POST'])
def vacaciones():
    if request.form['user_name'] == 'daraya':
        team.update_member_availability(
            member_tag=request.form['text'].strip(),
            available=False
        )
    return Response(), 200

@app.route('/fin-vacaciones', methods=['POST'])
def fin_vacaciones():
    if request.form['user_name'] == 'daraya':
        team.update_member_availability(
            member_tag=request.form['text'].strip(),
            available=True
        )
    return Response(), 200

@app.route('/marcar', methods=['POST'])
def marcar():
    print('request.form')
    print(request.form)
    rut = request.form.get('text').strip()
    bot.post(
        channel=request.form.get('user_id'),
        buttons=[
            {
                'text': 'Marcar entrada',
                'url': f'{links.url_marcar_entrada}{rut}',
            },
            {
                'text': 'Marcar salida',
                'url': f'{links.url_marcar_salida}{rut}',
                'style': 'danger'  # Optional: style can be 'primary' or 'danger'
            }
        ],
    )
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
