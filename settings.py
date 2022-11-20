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
XLSX_FILE = read_excel('dailies.xlsx', sheet_name='Table 2') 

# timezone local
TIME_ZONE = pytz.timezone('America/Santiago')
