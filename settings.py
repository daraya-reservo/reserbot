# Third Party
import dotenv

# Standard Library
import os
import pathlib


# ruta del proyecto
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

# cargar variables del archivo de ambiente .env
env_path = pathlib.Path('.') / '.env'
dotenv.load_dotenv(dotenv_path=env_path)
BOT_TOKEN = os.environ.get('SLACK_TOKEN')
SIGNING_SECRET = os.environ.get('SIGNING_SECRET')

# canales de slack
QA_CHANNEL = '#reserbot-shhhh'
MAIN_CHANNEL = '#reservo-ti'
DEBUG = False  # cambiar a True para usar QA_CHANNEL

# links relevantes
URL_EXCEL_LEARNING = 'https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit?gid=599070068#gid=599070068'
URL_MEET = 'https://meet.google.com/sft-muqe-ziq?authuser=0'
URL_TRELLO = 'https://trello.com/b/dZnTCMi3/tablero-desarrollo'

URL_MEET_REU_COMERCIAL = 'https://meet.google.com/kba-ivgs-heu'
URL_MEET_REU_CS = 'https://meet.google.com/rgc-uvjd-cqj'
URL_MEET_REU_SOPORTE = 'https://meet.google.com/ucg-ohck-hsx?authuser=1'
URL_MEET_REU_POSTVENTA = 'https://meet.google.com/ucg-ohck-hsx?authuser=1'
