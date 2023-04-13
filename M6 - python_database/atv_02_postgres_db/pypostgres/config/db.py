"""
Provides DOTENV CONFIG
"""

import psycopg2
from os import getenv
import dotenv

dotenv.load_dotenv()

db_connect = psycopg2.connect(
    host = getenv('DB_HOST'),
    port = getenv('DB_PORT'),
    database = getenv('DB_DATABASE'),
    user = getenv('DB_USER'),
    password = getenv('DB_PASSWORD')
)