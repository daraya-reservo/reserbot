# Reserbot
import settings

# Standard Library
import json
import random


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
    team_json = open(TEAM_MEMBERS_FILE, 'w')
    team_json.write(new_team)
    team_json.close()

class TeamManager:
    """Class to manage team members."""
    def __init__(self):
        with open(TEAM_MEMBERS_FILE) as team_members_file:
            self.members = json.load(team_members_file)
        self.random_pool = self.members.copy()

    def save(self):
        with open(TEAM_MEMBERS_FILE, 'w') as team_members_file:
            json.dump(self.members, team_members_file, indent=4)

    def update_disponibilidad(self, member_tag, available):
        for member in self.members:
            if member['tag'] == member_tag:
                member['is_available'] = available
        self.save()

    def get_daily_leader(self, day):
        team_members = [member for member in self.members if member['is_available']]
        # Exclude Hiho on Fridays
        if day.weekday() == 4:
            team_members = [member for member in team_members if member['name'] != 'Hiho']
        # Select the member with the lowest number of dailies
        leader = min(team_members, key=lambda member: member['dailies'])
        # Update the dailies count for the leader
        for member in self.members:
            if member['tag'] == leader['tag']:
                member['dailies'] += 1
                break
        self.save()
        return leader['tag']

    def get_random_leader(self, day):
        team_members = [member for member in self.random_pool if member['is_available']]
        # Exclude Hiho on Fridays
        if day.weekday() == 4:
            team_members = [member for member in team_members if member['name'] != 'Hiho']
        try:
            random_leader = random.choice(team_members)
        except IndexError:  # when random_leader_pool is empty
            return None
        self.random_pool.remove(random_leader)
        return random_leader['tag']

