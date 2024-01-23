from dotenv import load_dotenv
from pathlib import Path
import os

# cargar variables del archivo de ambiente .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
BOT_TOKEN = os.environ.get('SLACK_TOKEN')
SIGNING_SECRET = os.environ.get('SIGNING_SECRET')

# links relevantes
URL_ESTUDIO = 'https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit#gid=0'
URL_DISCORD = 'https://discord.com/channels/897964285559472158/1014947999010533416'
URL_TRELLO = 'https://trello.com/b/dZnTCMi3/tablero-desarrollo'
URL_NEWSLETTERS = 'https://www.notion.so/softwarereservo/Newsletter-semanal-a9fdabf7c2fc42e3ab0ea631da2e3b07'
