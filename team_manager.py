# Reserbot
import settings
import utils

# Standard Library
import json
import random


MEMBERS_JSON = f'{settings.PROJECT_ROOT}/members.json'

class TeamManager:

    def __init__(self):
        self.members = self.read_team_file()
        # Hiho is unavailable on Fridays
        if self.today.weekday() == 4:
            for member in self.members:
                if member['name'] == 'Hiho':
                    member['is_available'] = False
        self.random_pool = self.members.copy()
        self.today = utils.datetime_now()

    def read_team_file(self):
        with open(MEMBERS_JSON) as members_json:
            return json.load(members_json)

    def write_team_file(self, members):
        with open(MEMBERS_JSON, 'w') as members_json:
            json.dump(members, members_json, indent=4)

    def update_member_dailies(self, member_tag):
        members = self.read_team_file()
        for member in members:
            if member['tag'] == member_tag:
                member['dailies'] += 1
        self.write_team_file(members)

    def update_member_availability(self, member_tag, available):
        members = self.read_team_file()
        for member in members:
            if member['tag'] == member_tag:
                member['is_available'] = available
        self.write_team_file(members)

    def get_unavailable_members(self):
        return [member['name'] for member in self.members if not member['is_available']]

    def get_daily_leader(self):
        members = [member for member in self.members if member['is_available']]
        # Select the member with the lowest number of dailies
        leader = min(members, key=lambda member: member['dailies']).get('tag')
        self.update_member_dailies(member_tag=leader)
        return leader

    def get_random_leader(self):
        members = [member for member in self.random_pool if member['is_available']]
        if len(members) > 0:
            leader = random.choice(members)
            self.random_pool.remove(leader)
            return leader['tag']
        return None
