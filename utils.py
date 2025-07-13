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
        holidays_list = [holiday['date'] for holiday in holidays]
        # chequea que el día no esté en lista de feriados
        formatted_day = day.strftime('%Y-%m-%d')
        return formatted_day not in holidays_list

def get_leader():
    team = team_manager.get_team(available_only=True)
    # lidera el que tenga menor numero de dailies lideradas
    random.shuffle(team)
    leader = min(team, key=lambda member:member['dailies'])
    team_manager.update_dailies(leader['tag'])
    return leader['tag']

random_pool = team_manager.get_team(available_only=True)
def get_random_leader():
    global random_pool
    try:
        random_leader = random.choice(random_pool)
    except IndexError:  # cuando random_pool está vacia
        return None
    random_pool.remove(random_leader)
    return random_leader['tag']

def get_meeting(day):
    '''
    **Las reuniones disponibles son:**

    - Reunión área **comercial**: Todos los jueves a las 11:00 (presencial con opción online) - [](http://meet.google.com/kba-ivgs-heu)
    - Reunión **Soporte**: Viernes 16:30 (Online) - [https://meet.google.com/ucg-ohck-hsx](https://meet.google.com/ucg-ohck-hsx?authuser=1)
    - Reunión **customer success**: Viernes 10:30 (Online) - [meet.google.com/rgc-uvjd-cqj](http://meet.google.com/rgc-uvjd-cqj)
    - Reunión **TI, “daily”**: Lunes, martes, jueves, Viernes 9:15 - 9:30 (Online), Miércoles 10:00 - 10:15 (Presencial, pero nos conectamos igual :) ) - https://meet.google.com/sft-muqe-ziq
    - Reunión **Post venta**: Se realiza solo el primer Martes de cada mes a las 10:30)
    '''
    if day.weekday() == 3:
        return 'Hoy es la reunion del área comercial a las 11:00 aquí meet.google.com/kba-ivgs-heu'
    elif day.weekday() == 4:
        pass

