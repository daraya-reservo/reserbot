# Third Party
import dotenv

# Standard Library
import os
import pathlib

# cargar variables del archivo de ambiente .env
env_path = pathlib.Path('.') / '.env'
dotenv.load_dotenv(dotenv_path=env_path)
BOT_TOKEN = os.environ.get('SLACK_TOKEN')
SIGNING_SECRET = os.environ.get('SIGNING_SECRET')

# canales de slack
DEBUG_ENV = '#reserbot-shhhh'
PROD_ENV = '#reservo-ti'

# links relevantes
URL_EXCEL_LEARNING = 'https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit?gid=1385494284#gid=1385494284'
URL_MEET = 'https://meet.google.com/sft-muqe-ziq?authuser=0'
URL_TRELLO = 'https://trello.com/b/dZnTCMi3/tablero-desarrollo'

# ruta del proyecto
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
