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
import pytz
import random
import requests
import settings


def is_holiday(date):
    api_response = requests.get(f'{settings.URL_API_FERIADOS}{date.year}/CL')
    holidays = json.loads(api_response.content)
    return date.strftime('%Y-%m-%d') in holidays

def get_daily_leader():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    today = datetime.now(pytz.timezone('America/Santiago'))
    if today.weekday() >= 5 or is_holiday(today):
        return None

    settings.TEAM = dict(sorted(settings.TEAM.items(), key=operator.itemgetter(1)))
    teammates = settings.TEAM
    if today.weekday() == 0: 
        del teammates['Nach']
    elif today.weekday() == 3: 
        del teammates['Vicky']
    elif today.weekday() == 4: 
        del teammates['Vicky']
        del teammates['Hiho']

    daily_leader = next(iter(teammates))
    settings.TEAM[daily_leader] += 1
    return daily_leader

def get_random_teammate():
    teammates = list(settings.TEAM.keys())
    return random.choice(teammates)
