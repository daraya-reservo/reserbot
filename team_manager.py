# Reserbot
import settings

# Standard Library
import json


json_path = f'{settings.PROJECT_ROOT}/team.json'

def get_team(only_available=False, on_vacation=False):
    # abro archivo de integrantes del equipo
    with open(json_path) as json_team:
        team = json.load(json_team)
        # aplico filtros
        if only_available:
            team = [
                member for member in team 
                if member['is_available']
            ]
        elif on_vacation:
            team = [
                member for member in team 
                if not member['is_available']
            ]
        return team

def update_dailies(member_tag):
    team = get_team()
    for member in team:
        if member['tag'] == member_tag:
            member['dailies'] += 1
    _update_team(team)

def update_disponibilidad(member_tag):
    team = get_team()
    for member in team:
        if member['tag'] == member_tag:
            member['is_available'] = not member['is_available']
    _update_team(team)

def _update_team(team):
    team = json.dumps(team, indent=4)
    json_team = open(json_path, 'w')
    json_team.write(team)
    json_team.close()
