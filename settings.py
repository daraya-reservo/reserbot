from dotenv import load_dotenv
from pathlib import Path
import os

# cargar variables del archivo de ambiente .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
BOT_TOKEN = os.environ.get('SLACK_TOKEN')
SIGNING_SECRET = os.environ.get('SIGNING_SECRET')

# links relevantes
URL_ESTUDIO = 'https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit?gid=1385494284#gid=1385494284'
URL_MEET = 'https://meet.google.com/sft-muqe-ziq?authuser=0'
URL_TRELLO = 'https://trello.com/b/dZnTCMi3/tablero-desarrollo'
URL_NEWSLETTERS = 'https://www.notion.so/softwarereservo/Newsletter-semanal-a9fdabf7c2fc42e3ab0ea631da2e3b07'
URL_ENTRADA_SALIDA = 'https://app.ctrlit.cl/ctrl/dial/web/eJUVR0SMli'