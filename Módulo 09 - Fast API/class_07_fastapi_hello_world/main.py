from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv
from uvicorn import run

load_dotenv()

port = int(getenv('PORT'))

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

if __name__ == '__main__':
    run(app, host='localhost', port=port)