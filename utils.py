# Standard Library
import csv
import random

# Reserbot
import settings
import team_manager


def is_workday(day):
    # si el día es sábado(5) o domingo(6)
    if day.weekday() in [5, 6]:
        return False
    # abro archivo de feriados
    holidays_path = f'{settings.PROJECT_ROOT}/csv/publicholiday.CL.{day.year}.csv'  # ver README
    with open(holidays_path) as holidays_file:
        holidays = csv.DictReader(holidays_file)
        holidays_list = [holiday['Date'] for holiday in holidays]
        # chequea que el día no esté en lista de feriados
        formatted_day = day.strftime('%Y-%m-%d')
        return formatted_day not in holidays_list

def get_leader():
    team = team_manager.get_team(only_available=True)
    # lidera el que tenga menor numero de dailies lideradas
    random.shuffle(team)
    leader = min(team, key=lambda member:member['dailies'])
    return leader['tag']

random_pool = team_manager.get_team(only_available=True)

def get_random_leader():
    global random_pool
    try:
        random_leader = random.choice(random_pool)
    except IndexError:  # cuando random_pool está vacia
        return None
    random_pool.remove(random_leader)
    return random_leader['name']
