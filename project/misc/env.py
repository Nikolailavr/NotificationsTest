import os
from typing import Final
# from dotenv import load_dotenv

# load_dotenv('.env')

EMAIL_TO = os.environ.get('EMAIL')


class DBSettings:
    PORT: Final = os.environ.get('DB_PORT')
    HOST: Final = os.environ.get('DB_URL')


class EmailSettings:
    HOST: Final = os.environ.get('SMTP_HOST')
    PORT: Final = os.environ.get('SMTP_PORT')
    LOGIN: Final = os.environ.get('SMTP_LOGIN')
    PASSWORD: Final = os.environ.get('SMTP_PASSWORD')
    EMAIL: Final = os.environ.get('SMTP_EMAIL')
    NAME: Final = os.environ.get('SMTP_NAME')
