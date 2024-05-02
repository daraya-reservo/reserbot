import csv
import json
import operator
import os
import random


def working_day(today):
    project_path = os.path.realpath(os.path.dirname(__file__))
    csv_holidays = f'{project_path}/csv/publicholiday.CL.{today.year}.csv'
    with open(csv_holidays, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Date'] == today.strftime('%Y-%m-%d'):
                return False
    return today.weekday() < 5

def get_team():
    project_path = os.path.realpath(os.path.dirname(__file__))
    with open(f'{project_path}/team.json', 'r') as json_file:
        team_as_dict = json.load(json_file)
    return team_as_dict

def update_team(team_as_dict):
    project_path = os.path.realpath(os.path.dirname(__file__))
    team_as_json = json.dumps(team_as_dict, indent=4)
    with open(f'{project_path}/team.json', 'w') as json_file:
        json_file.write(team_as_json)

def get_daily_leader(today):
    if not working_day(today):
       return ''
    team = get_team()
    team_members = list(team.items())
    random.shuffle(team_members)
    teammates = dict(sorted(dict(team_members).items(), key=operator.itemgetter(1)))
    if today.weekday() == 0:
        # lunes Nach no trabaja
        teammates = {key: teammates[key] for key in teammates if key != 'Nach'}
    elif today.weekday() == 3:
        # jueves Vicky en área de ventas
        teammates = {key: teammates[key] for key in teammates if key != 'Vicky'}
    elif today.weekday() == 4:
        # viernes no están Hiho ni Vicky
        teammates = {key: teammates[key] for key in teammates if key != 'Vicky'}
    daily_leader = next(iter(teammates))
    team[daily_leader] += 1
    update_team(team)
    return daily_leader

def get_random_teammate():
    team = get_team()
    teammates = list(team.keys())
    return random.choice(teammates)
