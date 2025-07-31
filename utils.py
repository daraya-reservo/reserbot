# Standard Library
import csv
from datetime import datetime
import locale

# Third Party
import pytz

# Reserbot
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
