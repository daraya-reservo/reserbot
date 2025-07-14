# Reserbot
import settings

# Standard Library
import json


TEAM_MEMBERS_FILE = f'{settings.PROJECT_ROOT}/team_members.json'

def get_team(available_only=False, on_vacation=False):
    # abro archivo de integrantes del equipo
    with open(TEAM_MEMBERS_FILE) as team_members_file:
        team_members = json.load(team_members_file)
        # aplico filtros
        if available_only:
            team_members = [
                member for member in team_members 
                if member['is_available']
            ]
        elif on_vacation:
            team_members = [
                member for member in team_members 
                if not member['is_available']
            ]
        return team_members

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

class TeamManager:
    """Class to manage team members."""
    def __init__(self):
        with open(TEAM_MEMBERS_FILE) as team_members_file:
            self.team = json.load(team_members_file)

    def get_members(self, available_only=False, on_vacation=False):
        return self.team

    def update_dailies(self, member_tag):
        update_dailies(member_tag)

    def update_disponibilidad(self, member_tag, available):
        update_disponibilidad(member_tag, available)
