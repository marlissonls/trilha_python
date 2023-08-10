from fastapi import FastAPI
from dotenv import load_dotenv
from uvicorn import run
from configs import host, port

load_dotenv()

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

if __name__ == '__main__':
    run(app, host=host, port=port)