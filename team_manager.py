# Reserbot
import settings

# Standard Library
import json


TEAM_JSON = f'{settings.PROJECT_ROOT}/team.json'

def get_team(available_only=False, on_vacation=False):
    # abro archivo de integrantes del equipo
    with open(TEAM_JSON) as team_json:
        team = json.load(team_json)
        # aplico filtros
        if available_only:
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

def update_disponibilidad(member_tag, available):
    team = get_team()
    for member in team:
        if member['tag'] == member_tag:
            member['is_available'] = available
    _update_team(team)

def _update_team(team):
    new_team = json.dumps(team, indent=4)
    team_json = open(TEAM_PATH, 'w')
    team_json.write(new_team)
    team_json.close()
