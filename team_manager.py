# Reserbot
import settings

# Standard Library
import csv
import datetime
import json
import random


class TeamManager:

    team_path = f'{settings.PROJECT_ROOT}/team.json'

    def __init__(self, today: datetime.datetime):
        self.today = today
        self.team = self._read_team_file()
        # Hiho isn't available on friday
        if self.today.weekday() == 4:
            for member in self.team:
                if member['name'] == 'Hiho':
                    member['is_available'] = False
        self.random_pool = self.team.copy()

    def _read_team_file(self) -> list:
        with open(self.team_path) as team:
            return json.load(team)

    def _write_team_file(self, team: list) -> None:
        with open(self.team_path, 'w') as team_file:
            json.dump(team, team_file, indent=4)

    def update_member_dailies(self, member_tag: str) -> None:
        team = self._read_team_file()
        for member in team:
            if member['tag'] == member_tag:
                member['dailies'] += 1
        self._write_team_file(team)

    def update_member_availability(
            self,
            member_tag: str,
            available: bool
        ) -> None:
        team = self._read_team_file()
        for member in team:
            if member['tag'] == member_tag:
                member['is_available'] = available
        self._write_team_file(team)

    def update_member_rut(self, member_tag: str, rut: str) -> None:
        team = self._read_team_file()
        for member in team:
            if member['tag'] == member_tag:
                member['rut'] = rut
        self._write_team_file(team)

    def is_workday(self):
        if self.today.weekday() not in range(5):
            return False
        holidays_path = f'{settings.PROJECT_ROOT}/csv/publicholiday.CL.{self.today.year}.csv'
        with open(holidays_path) as holidays_file:
            holidays = csv.DictReader(holidays_file)
            holidays_list = [holiday['date'] for holiday in holidays]
        return self.today.strftime('%Y-%m-%d') not in holidays_list
    
    def get_members_with_rut(self):
        return [member for member in self.team if member['rut']]

    def get_unavailable_members(self):
        return [member['name'] for member in self.team if not member['is_available']]

    def get_daily_leader(self):
        team = [member for member in self.team if member['is_available']]
        # Select the member with the lowest number of dailies
        leader = min(team, key=lambda member: member['dailies']).get('tag')
        self.update_member_dailies(member_tag=leader)
        return leader

    def get_random_daily_leader(self):
        team = [member for member in self.random_pool if member['is_available']]
        if not team:
            return
        leader = random.choice(team)
        self.random_pool.remove(leader)
        return leader['tag']
 