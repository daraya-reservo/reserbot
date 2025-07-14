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

    def get_team_members(self, day, available=True):
        team_members = [member for member in self.team if member['is_available'] == available]
        # Exclude Hiho on Fridays
        if day.weekday() == 4:
            team_members = [member for member in team_members if member['name'] != 'Hiho']
        return team_members

    def save(self):
        with open(TEAM_MEMBERS_FILE, 'w') as team_members_file:
            json.dump(self.team, team_members_file, indent=4)

    def update_dailies(self, member_tag):
        for member in self.team:
            if member['tag'] == member_tag:
                member['dailies'] += 1
        self.save()

    def update_disponibilidad(self, member_tag, available):
        for member in self.team:
            if member['tag'] == member_tag:
                member['is_available'] = available
        self.save()
