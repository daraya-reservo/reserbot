# Reserbot
import settings
import utils

# Standard Library
import json
import random


MEMBERS_JSON = f'{settings.PROJECT_ROOT}/members.json'

class TeamManager:
    """Class to manage team members."""
    def __init__(self):
        with open(MEMBERS_JSON) as members_json:
            self.members = json.load(members_json)
        self.today = utils.datetime_now()
        self.random_pool = self.members.copy()

    def save_members(self):
        with open(MEMBERS_JSON, 'w') as members_json:
            json.dump(self.members, members_json, indent=4)

    def get_unavailable_members(self, day):
        unavailable_members = {member['name'] for member in self.members if not member['is_available']}
        # Include Hiho on Fridays (unavailable for today)
        if day.weekday() == 4:
            unavailable_members.add('Hiho')
        return unavailable_members

    def get_daily_leader(self, day):
        members = [member for member in self.members if member['is_available']]
        # Exclude Hiho on Fridays
        if day.weekday() == 4:
            members = [member for member in members if member['name'] != 'Hiho']
        # Select the member with the lowest number of dailies
        leader = min(members, key=lambda member: member['dailies'])
        # Update the dailies count for the leader
        for member in self.members:
            if member['tag'] == leader['tag']:
                member['dailies'] += 1
                break
        self.save_members()
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

    def update_availability(self, member_tag, available):
        for member in self.members:
            if member['tag'] == member_tag:
                member['is_available'] = available
        self.save_members()

