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


def working_day():
    print('==================================')
    print('working_day()')
    print('==================================')
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    today = datetime.now(pytz.timezone('America/Santiago'))
    print('holidays_url: ', f'{settings.URL_API_FERIADOS}{today.year}/CL')
    holidays_resp = requests.get(
        f'{settings.URL_API_FERIADOS}{today.year}/CL',
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0'
        }    
    )
    holidays = json.loads(holidays_resp.content)
    print('holidays: ', holidays)
    today_not_holiday = today.strftime('%Y-%m-%d') not in holidays
    today_not_weekend = today.weekday() < 5
    return today_not_holiday and today_not_weekend


def get_daily_leader():
    print('==================================')
    print('get_daily_leader()')
    print('==================================')
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    today = datetime.now(pytz.timezone('America/Santiago'))
    #if not working_day():
    #    return ''

    team_members = list(settings.TEAM.items())
    random.shuffle(team_members)
    settings.TEAM = dict(team_members)
    settings.TEAM = dict(sorted(settings.TEAM.items(), key=operator.itemgetter(1)))
    teammates = settings.TEAM
    if today.weekday() == 0:
        del teammates['Nach']
    elif today.weekday() == 3:
        del teammates['Vicky']
    elif today.weekday() == 4:
        del teammates['Vicky']
        del teammates['Hiho']
    print("teammates", teammates)

    daily_leader = next(iter(teammates))
    settings.TEAM[daily_leader] += 1
    print("settings.TEAM" , settings.TEAM)
    print('==================================')
    print('end of get_daily_leader()')
    print('==================================')
    return daily_leader

def get_random_teammate():
    teammates = list(settings.TEAM.keys())
    return random.choice(teammates)
