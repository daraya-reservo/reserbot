from dotenv import load_dotenv
from pathlib import Path
import os


# cargar variables del archivo de ambiente .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
BOT_TOKEN = os.environ['SLACK_TOKEN']
SIGNING_SECRET = os.environ['SIGNING_SECRET']

# canales a los que se envían mensajes
CHANNEL_PROD = '#reservo-ti'
CHANNEL_DEV = '#reserbot-shhhh'

# links relevantes
URL_EXCEL_ESTUDIO = 'https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit#gid=0'
URL_DISCORD_DAILY = 'https://discord.com/channels/897964285559472158/1014947999010533416'
URL_TRELLO = 'https://trello.com/b/dZnTCMi3/tablero-desarrollo'
URL_API_FERIADOS = 'https://date.nager.at/api/v3/publicholidays/'
URL_NOTION_NEWSLETTERS = 'https://www.notion.so/softwarereservo/Newsletter-semanal-a9fdabf7c2fc42e3ab0ea631da2e3b07'

TEAM = {
    'Agustín': 0,
    'Dani': 0,
    'Juan': 0,
    'Hiho': 0,
    'Lucho': 0,
    'Manu': 0,
    'Nach': 0,
    'Pancho': 0,
    'Pato': 0,
    'Seba': 0,
    'Val': 0,
    'Vicky': 0,
}