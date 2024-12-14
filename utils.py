import csv
import json
import operator
import os
import random


def rest_day(today):
    if today.weekday() in [5, 6]:
        return True
    project_path = os.path.realpath(os.path.dirname(__file__))
    holidays_path = f'{project_path}/csv/publicholiday.CL.{today.year}.csv'
    with open(holidays_path) as holidays_file:
        holidays = csv.DictReader(holidays_file)
        formatted_day = today.strftime('%Y-%m-%d')
        return formatted_day in [day['Date'] for day in holidays]

def get_team():
    project_path = os.path.realpath(os.path.dirname(__file__))
    with open(f'{project_path}/team.json', 'r') as json_file:
        team_as_dict = json.load(json_file)
    return team_as_dict

def update_team(team_as_dict):
    project_path = os.path.realpath(os.path.dirname(__file__))
    team_as_json = json.dumps(team_as_dict, indent=4)
    with open(f'{project_path}/team.json', 'w') as json_file:
        json_file.write(team_as_json)

def get_lider_daily(today):
    if rest_day(today):
       return None
    team = get_team()
    members = list(team.items())
    random.shuffle(members)
    teammates = dict(sorted(dict(members).items(), key=operator.itemgetter(1)))
    daily_leader = next(iter(teammates))
    team[daily_leader] += 1
    update_team(team)
    return daily_leader

def get_lider_random(team_members):
    lider_random = random.choice(team_members)
    team_members.remove(lider_random)
    return lider_random, team_members

def build_message(text=None, buttons=None):
    message = []
    if text:
        message.append({
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': text
            }
        })
    if buttons:
        btn_elements = [{
            'type': 'button',
            'text': {
                'type': 'plain_text',
                'text': button['text'],
                'emoji': True
            },
            'style': 'primary',
            'url': button['url']
        } for button in buttons]
        message.append({
            'type': 'actions',
            'elements': btn_elements
        })
    return message