from uvicorn import run
from configs import configs

port: int = configs["port"]

if __name__ == '__main__':
    run("app:api", port=port)