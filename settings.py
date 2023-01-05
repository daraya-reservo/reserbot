import os
import pytz
from pandas import read_excel
from pathlib import Path
from dotenv import load_dotenv


# cargar variables del archivo de ambiente .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
BOT_TOKEN = os.environ['SLACK_TOKEN']
SIGNING_SECRET = os.environ['SIGNING_SECRET']

# obtener dataframe del archivo excel
reserbot_path = os.path.realpath(os.path.dirname(__file__))
XLSX_FILE = read_excel(f'{reserbot_path}/dailies.xlsx', sheet_name='Hoja1')

# timezone local
TIME_ZONE = pytz.timezone('America/Santiago')

# channel to post to
CHANNEL_PROD = '#reservo-ti'
CHANNEL_DEV = '#reserbot-shhhh'
