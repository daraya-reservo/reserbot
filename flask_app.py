# Third Party
from flask import Flask, request, Response, jsonify, redirect
from slackeventsapi import SlackEventAdapter

# Reserbot
import settings
from bot_manager import BotManager
from team_manager import TeamManager
import utils


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(settings.SIGNING_SECRET, '/slack/events', app)
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
            'url': 'https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit?gid=599070068#gid=599070068'
        }],
    )
    return Response(), 200

@app.route('/lider-al-azar', methods=['POST'])
def lider_al_azar():
    user = request.form.get('user_name')
    today = utils.datetime_now()
    random_leader = team.get_random_leader(today)
    if random_leader:
        reserbot.post_message(
            text=f'@{user} pidió un lider al azar: lidera {random_leader} :rubyrun:'
        )
    return Response(), 200

def _actualizar_vacaciones(request, available):
    user = request.form.get('user_name')
    member_tag = request.form.get('text').strip()
    if user == 'daraya':
        team.update_availability(
            member_tag=member_tag,
            available=available
        )

@app.route('/vacaciones', methods=['POST'])
def vacaciones():
    _actualizar_vacaciones(request, available=False)
    return Response(), 200

@app.route('/fin-vacaciones', methods=['POST'])
def fin_vacaciones():
    _actualizar_vacaciones(request, available=True)
    return Response(), 200

@app.route('/marcar-entrada', methods=['POST'])
def marcar_entrada():
    rut = request.form.get('text').strip()
    url = f'https://app.ctrlit.cl/ctrl/dial/registrarweb/eJUVR0SMli?sentido=1&rut={rut}'
    response = redirect(url)
    return redirect(url), 200

@app.route('/marcar-salida', methods=['POST'])
def marcar_salida():
    rut = request.form.get('text').strip()
    url = f'https://app.ctrlit.cl/ctrl/dial/registrarweb/eJUVR0SMli?sentido=0&rut={rut}'
    return redirect(url), 200

if __name__ == '__main__':
    app.run(port=5000)


"""
@app.route('/slack/events', methods=['POST'])
def events():
    return jsonify(challenge=request.get_json().get('challenge', ''))

"""
