from os import getenv
from dotenv import load_dotenv

load_dotenv()

configs = {
    'host': getenv('HOST'),
    'port': int(getenv('PORT'))
}
