# Standard Library
import csv
from datetime import datetime
import locale

# Third Party
import pytz

# Reserbot
import settings


def get_local_datetime_now():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    return datetime.now(pytz.timezone('America/Santiago'))

def is_workday(day):
    # si el día es sábado(5) o domingo(6)
    if day.weekday() in [5, 6]:
        return False
    # abro archivo de feriados
    holidays_path = f'{settings.PROJECT_ROOT}/csv/publicholiday.CL.{day.year}.csv'  # ver README
    with open(holidays_path) as holidays_file:
        holidays = csv.DictReader(holidays_file)
        holidays_list = [holiday['date'] for holiday in holidays]
        # chequea que el día no esté en lista de feriados
        formatted_day = day.strftime('%Y-%m-%d')
        return formatted_day not in holidays_list

def get_meetings(day):
    meetings = []
    # primer martes del mes
    if day.weekday() == 1 and day.day in range(7):
        meetings.append({
            'text': f'Hoy es la reunión del área de Postventa a las 10:30 AM',
            'url': 'https://meet.google.com/pct-qnin-cgp',
        })
    # jueves
    elif day.weekday() == 3:
        meetings.append({
            'text': f'Hoy es la reunión del área Comercial a las 11:00 AM',
            'url': 'https://meet.google.com/kba-ivgs-heu',
        })
    # viernes
    elif day.weekday() == 4:
        meetings.append({
            'text': f'Hoy es la reunión del área de Customer Success a las 10:30 AM',
            'url': 'https://meet.google.com/rgc-uvjd-cqj',
        })
        meetings.append({
            'text': f'Hoy es la reunión del área de Soporte a las 16:30 PM',
            'url': 'https://meet.google.com/ucg-ohck-hsx',
        })
    return meetings
