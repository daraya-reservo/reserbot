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


def is_working_day():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    today = datetime.now(pytz.timezone('America/Santiago'))
    project_path = os.path.realpath(os.path.dirname(__file__))
    csv_holidays = f'{project_path}/csv/publicholiday.CL.{today.year}.csv'
    with open(csv_holidays, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Date'] == today.strftime('%Y-%m-%d'):
                return False
    return today.weekday() < 5


def get_daily_leader():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    today = datetime.now(pytz.timezone('America/Santiago'))
    #if is_working_da|y() is False:
    #    return ''

    team_members = list(settings.TEAM.items())
    random.shuffle(team_members)
    settings.TEAM = dict(team_members)
    settings.TEAM = dict(sorted(settings.TEAM.items(), key=operator.itemgetter(1)))
    teammates = settings.TEAM
    if today.weekday() == 0:
        teammates = {key: teammates[key] for key in teammates if key != 'Nach'}
    elif today.weekday() == 3:
        teammates = {key: teammates[key] for key in teammates if key != 'Vicky'}
    elif today.weekday() == 4:
        teammates = {key: teammates[key] for key in teammates if key not in ('Vicky', 'Hiho')}
    print("teammates", teammates)

    daily_leader = next(iter(teammates))
    settings.TEAM[daily_leader] += 1
    print("settings.TEAM" , settings.TEAM)
    return daily_leader

def get_random_teammate():
    teammates = list(settings.TEAM.keys())
    return random.choice(teammates)
