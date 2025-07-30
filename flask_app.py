# Third Party
from flask import Flask, request, Response, jsonify, redirect
from slackeventsapi import SlackEventAdapter

# Reserbot
import links
import settings
from bot_manager import BotManager
from team_manager import TeamManager


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)
team = TeamManager()
reserbot = BotManager(token=settings.BOT_TOKEN)


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
    reserbot.post(
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
        reserbot.post(
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
    url_entrada = f'{links.url_marcar_entrada}{rut}'
    url_salida = f'{links.url_marcar_salida}{rut}'
    reserbot.post(
        text=f'@{request.form["user_name"]} quiere marcar su entrada/salida :finoseñores:',
        buttons=[
            {
                'text': 'Marcar entrada',
                'url': url_entrada,
            },
            {
                'text': 'Marcar salida',
                'url': url_salida,
                'style': 'danger'  # Optional: style can be 'primary' or 'danger'
            }
        ],
        production=False
    )
    return Response(), 200

if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
