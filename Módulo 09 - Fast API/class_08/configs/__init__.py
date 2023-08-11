from os import getenv

configs = {
    'host': getenv('HOST'),
    'port': int(getenv('PORT'))
}
