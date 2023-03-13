from datetime import datetime, timedelta
from random import choice
import locale
import os
import pandas


def lider_random():
    team = ('Agustín', 'Dani', 'Hiho', 'Lucho', 'Manu', 'Pancho', 'Pato', 'Seba', 'Val')
    return f'Que lidere {choice(team)} :rubyrun:'


def lider_daily():
    project_path = os.path.realpath(os.path.dirname(__file__))
    excel_dailies = pandas.read_excel(f'{project_path}/dailies.xlsx', sheet_name='Hoja1')  # obtener dataframe del archivo excel
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # para setear el lenguaje en el server
    lider_daily = excel_dailies[excel_dailies['Día'] == datetime.now().strftime('%Y-%m-%d')]['Responsable'].values
    return f'Hoy {datetime.now().strftime("%A %d")} lidera {lider_daily[0]} :finoseñores:' if lider_daily.size else None


def lider_siguiente():
    project_path = os.path.realpath(os.path.dirname(__file__))
    excel_dailies = pandas.read_excel(f'{project_path}/dailies.xlsx', sheet_name='Hoja1') # obtener dataframe del archivo excel
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # para setear el lenguaje en el server
    dia_siguiente = datetime.now() + timedelta(days=1)
    lider_daily = excel_dailies[excel_dailies['Día'] == dia_siguiente.strftime('%Y-%m-%d')]['Responsable'].values
    return f'Mañana {dia_siguiente.strftime("%A %d")} lidera {lider_daily[0]} :ola2:' if lider_daily.size else f'Mañana {dia_siguiente.strftime("%A")} no hay daily :shirabesleep:'
