from uvicorn import run
from app.configs import configs

port: int = configs["port"]

if __name__ == '__main__':
    run("app:api", port=port)