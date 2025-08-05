# Reserbot
import links
import slack_manager
import team_manager

# Standard Library
import datetime
import locale

# Third Party
import pytz


class Controller:

    channels = {
        'PROD': '#reservo-ti',
        'TEST': '#reserbot-shhhh',
    }

    def __init__(self):
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        self.today = datetime.datetime.now(pytz.timezone('America/Santiago'))
        self.slack = slack_manager.SlackManager()
        self.team = team_manager.TeamManager(self.today)
        self.schedule_channel = self.channels['PROD']

    # flask_app logic controller
    def post_message_estudio(self, data: dict) -> None:
        user = data['user_name']
        channel = data['channel_name']
        self.slack.post(
            channel=channel,
            text=f'@{user} va a tomar la hora de estudio :rubyhappy: anótate :bonk-doge:',
            buttons=[{
                'text': 'Ir al excel 📚',
                'url': links.url_excel_estudio
            }],
        )

    def post_message_lider_al_azar(self, data: dict) -> None:
        user = data['user_name']
        channel = data['channel_name']
        random_leader = self.team.get_random_daily_leader()
        if random_leader:
            self.slack.post(
                channel=channel,
                text=f'@{user} pidió un lider al azar: lidera {random_leader} :rubyrun:'
            )

    def update_member_availability(self, data: dict, available: bool) -> None:
        user = data['user_name']
        member_tag = data['text'].strip()
        if user == 'daraya':
            self.team.update_member_availability(
                member_tag=member_tag,
                available=available
            )

    def suscribir_rut(self, data: dict) -> None:
        rut = data['text'].strip()
        member_tag = f'@{data["user_name"]}'
        self.team.update_member_rut(
            member_tag=member_tag,
            rut=rut
        )

    def desuscribir_rut(self, data: dict) -> None:
        member_tag = f'@{data["user_name"]}'
        self.team.update_member_rut(
            member_tag=member_tag,
            rut=''
        )

    # schedule logic controller
    def is_workday(self) -> bool:
        return self.team.is_workday()

    def schedule_message_marcar(self) -> None:
        members_with_rut = [member for member in self.team if member['rut']]
        for member in members_with_rut:
            self.slack.post(
                channel=member['tag'],
                buttons=[
                    {
                        'text': 'Marcar entrada',
                        'url': links.url_marcar_entrada + member['rut']
                    },
                ],
                post_at=self.today.replace(hour=8, minute=55, second=0).strftime('%s')
            )
            self.slack.post(
                channel=member['tag'],
                buttons=[
                    {
                        'text': 'Marcar salida',
                        'url': links.url_marcar_salida + member['rut'],
                        'style': 'danger'
                    },
                ],
                post_at=self.today.replace(hour=17, minute=55, second=0).strftime('%s')
            )

    def schedule_message_unavailable_members(self) -> None:
        unavailable_members = self.team.get_unavailable_members()
        if unavailable_members:
            self.slack.post(
                channel=self.schedule_channel,
                text=f'Hoy no estará: {", ".join(unavailable_members)} :f2:',
                post_at=self.today.replace(hour=9, minute=0, second=0).strftime('%s')
            )

    def schedule_message_daily_leader(self) -> None:
        leader = self.team.get_daily_leader()
        self.slack.post(
            channel=self.schedule_channel,
            text=f'Hoy {self.today.strftime("%A %d")} lidera {leader} :anime:',
            buttons=[
                {
                    "text": "Abrir Trello :trello:",
                    "url": links.url_trello,
                },
                {
                    "text": "Unirse a Meet :meet:",
                    "url": links.url_meet_daily,
                },
            ],
            post_at=self.today.replace(hour=9, minute=1, second=0).strftime('%s')
        )

    def schedule_message_meetings(self) -> None:
        # primer martes del mes
        if self.today.weekday() == 1 and self.today.day in range(7):
            self.slack.post(
                channel=self.schedule_channel,
                text='Hoy es la reunión del área de Postventa a las 10:30 AM',
                buttons=[{
                    'text': 'Unirse a la reunión :meet:',
                    'url': links.url_meet_postventa
                }],
                post_at=self.today.replace(hour=9, minute=35, second=0).strftime('%s')
            )
        # jueves
        elif self.today.weekday() == 3:
            self.slack.post(
                channel=self.schedule_channel,
                text='Hoy es la reunión del área Comercial a las 11:00 AM',
                buttons=[{
                    'text': 'Unirse a la reunión :meet:',
                    'url': links.url_meet_comercial
                }],
                post_at=self.today.replace(hour=10, minute=0, second=0).strftime('%s')
            )
        # viernes
        elif self.today.weekday() == 4:
            self.slack.post(
                channel=self.schedule_channel,
                text='Hoy es la reunión del área de Customer Success a las 10:30 AM',
                buttons=[{
                    'text': 'Unirse a la reunión :meet:',
                    'url': links.url_meet_customer_success
                }],
                post_at=self.today.replace(hour=9, minute=30, second=30).strftime('%s')
            )
            self.slack.post(
                channel=self.schedule_channel,
                text='Hoy es la reunión del área de Soporte a las 16:30 PM',
                buttons=[{
                    'text': 'Unirse a la reunión :meet:',
                    'url': links.url_meet_soporte
                }],
                post_at=self.today.replace(hour=9, minute=31, second=0).strftime('%s')
            )
