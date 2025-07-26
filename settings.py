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

DEBUG = False  # si es True usa canal de pruebas
