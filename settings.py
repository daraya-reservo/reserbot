from dotenv import load_dotenv
from pathlib import Path
import os


# cargar variables del archivo de ambiente .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
BOT_TOKEN = os.environ['SLACK_TOKEN']
SIGNING_SECRET = os.environ['SIGNING_SECRET']

# canales para postear mensajes
CHANNEL_PROD = '#reservo-ti'
CHANNEL_DEV = '#reserbot-shhhh'

# api key de openai
API_KEY = os.environ.get('OPENAI_APIKEY')
