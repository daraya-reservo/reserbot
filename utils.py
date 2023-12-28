from datetime import datetime
import locale
import os
import pandas
import pytz


def lider_daily():
    project_path = os.path.realpath(os.path.dirname(__file__))
    excel_path = f'{project_path}/dailies.xlsx'
    excel_dailies = pandas.read_excel(excel_path, sheet_name='Hoja1')
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    today = datetime.now(pytz.timezone('America/Santiago')).strftime('%Y-%m-%d')
    lider_daily = excel_dailies[excel_dailies['Día'] == today]['Responsable'].values
    return lider_daily[0] if lider_daily.size else None


from datetime import datetime
import json
import locale
import operator
import os
import pytz
import random
import requests
import settings
import csv


def is_working_day(date_input):
    project_path = os.path.realpath(os.path.dirname(__file__))
    csv_holidays = f'{project_path}/csv/publicholiday.CL.{date_input.year}.csv'
    with open(csv_holidays, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Date'] == date_input.strftime('%Y-%m-%d'):
                return False
    return date_input.weekday() < 5


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


def get_daily_leader():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    today = datetime.now(pytz.timezone('America/Santiago'))
    if not is_working_day(today):
       return ''
    team = get_team()
    team_members = list(team.items())
    random.shuffle(team_members)
    teammates = dict(sorted(dict(team_members).items(), key=operator.itemgetter(1)))
    if today.weekday() == 0:
        teammates = {key: teammates[key] for key in teammates if key != 'Nach'}
    elif today.weekday() == 3:
        teammates = {key: teammates[key] for key in teammates if key != 'Vicky'}
    elif today.weekday() == 4:
        teammates = {key: teammates[key] for key in teammates if key not in ('Hiho', 'Vicky')}
    daily_leader = next(iter(teammates))
    team[daily_leader] += 1
    update_team(team)
    return daily_leader


def get_random_teammate():
    team = get_team()
    teammates = list(team.keys())
    return random.choice(teammates)
