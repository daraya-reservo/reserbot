from datetime import datetime
import locale
import os
import pandas
import pytz


def lider_daily():
    project_path = os.path.realpath(os.path.dirname(__file__))
    excel_path = f'{project_path}/dailies.xlsx'
    # obtener dataframe del archivo excel
    excel_dailies = pandas.read_excel(excel_path, sheet_name='Hoja1')
    # setear el lenguaje en el server
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    today = datetime.now(pytz.timezone('America/Santiago')).strftime('%Y-%m-%d')
    lider_daily = excel_dailies[excel_dailies['Día'] == today]['Responsable'].values
    return lider_daily[0] if lider_daily.size else None


import json
import requests
import settings


def can_lead_today(member, day):
    nach_on_monday = member == 'Nach' and day.weekday() == 0
    hiho_on_friday = member == 'Hiho' and day.weekday() == 4
    vicky_on_thu_fri = member == 'Vicky' and day.weekday() in (3, 4)
    is_able_to_lead = not(
        nach_on_monday or
        vicky_on_thu_fri or
        hiho_on_friday
    )
    return is_able_to_lead


def get_daily_leader():
    today = datetime.now(pytz.timezone('America/Santiago'))
    today_is_weekend = today.weekday() >= 5
    holidays_response = requests.get(f'{settings.URL_API_FERIADOS}{today.year}/CL')
    holidays = json.loads(holidays_response.content)
    today_is_holiday = today.strftime('%Y-%m-%d') in holidays
    if today_is_weekend or today_is_holiday:
        return None
    settings.TEAM.sort(key=lambda item: item[1])
    if today.weekday() == 0:
        daily_leader = list(filter(lambda x:x[0]!='Nach', settings.TEAM))[0][0]
    elif today.weekday() == 3:
        daily_leader = list(filter(lambda x:x[0]!='Vicky', settings.TEAM))[0][0]
    elif today.weekday() == 4:
        daily_leader = list(filter(lambda x:x[0]not in ['Vicky', 'Hiho'], settings.TEAM))[0][0]
    else:
        daily_leader = settings.TEAM[0][0]
    settings.TEAM = []
    



