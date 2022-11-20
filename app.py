from flask import Flask, request, Response, jsonify
from utils import slack_simple_message, get_daily_leader, slack_button_message, bot_id, next_daily
# from slackeventsapi import SlackEventAdapter
# from settings import SIGNING_SECRET


app = Flask(__name__)
# slack_events_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)

@app.route('/', methods=['GET', 'POST'])
def index():
    print('request:', vars(request))
    return jsonify(success=True, message='Bot de Reservo. Wenas!')

@app.route('/daily', methods=['POST'])
def daily():
    channel = request.form.get('channel_name')
    msg = get_daily_leader()
    slack_simple_message(channel=f'#{channel}', message=msg if msg else 'Hoy no hay daily')
    return Response(), 200


@app.route('/next', methods=['POST'])
def next():
    channel = request.form.get('channel_name')
    msg = next_daily()
    slack_simple_message(channel=f'#{channel}', message=msg if msg else 'Hoy no hay daily')
    return Response(), 200


@app.route('/estudio', methods=['POST'])
def estudio():
    channel = request.form.get('channel_name')
    msg = f"Planeas tomar tiempo de estudio hoy? :estudio: "
    btn = "Anotarse en el excel"
    btn_link = "https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit?usp=sharing"    
    slack_button_message(channel=f'#{channel}', message=msg, button_text=btn, link=btn_link)
    return Response(), 200

# @slack_events_adapter.on('message')
# def message(payload):
#     print(23456)
#     print(payload)
#     event = payload.get('event', {})
#     channel_id = event.get('channel')
#     user_id = event.get('user')
#     text = event.get('text')
#     if bot_id != user_id:
#         client.chat_postMessage(channel=channel_id, text=text)



if __name__ == '__main__':
    app.run(port=5000)