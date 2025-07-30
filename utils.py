# Standard Library
import csv
from datetime import datetime
import locale

# Third Party
import pytz

# Reserbot
import links
import settings


def datetime_now():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    return datetime.now(pytz.timezone('America/Santiago'))

def feriados(year):
    # abro archivo de feriados
    holidays_path = f'{settings.PROJECT_ROOT}/csv/publicholiday.CL.{year}.csv'  # ver README
    with open(holidays_path) as holidays_file:
        holidays = csv.DictReader(holidays_file)
        return [holiday['date'] for holiday in holidays]

def get_meetings(day):
    meetings = []
    # primer martes del mes
    if day.weekday() == 1 and day.day in range(7):
        meetings.append({
            'text': f'Hoy es la reunión del área de Postventa a las 10:30 AM',
            'url': links.url_meet_postventa,
        })
    # jueves
    elif day.weekday() == 3:
        meetings.append({
            'text': f'Hoy es la reunión del área Comercial a las 11:00 AM',
            'url': links.url_meet_comercial,
        })
    # viernes
    elif day.weekday() == 4:
        meetings.append({
            'text': f'Hoy es la reunión del área de Customer Success a las 10:30 AM',
            'url': links.url_meet_customer_success,
        })
        meetings.append({
            'text': f'Hoy es la reunión del área de Soporte a las 16:30 PM',
            'url': links.url_meet_soporte,
        })
    return meetings
