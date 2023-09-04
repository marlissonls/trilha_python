from sqlalchemy.orm import sessionmaker
from app.configs import engine

Session = sessionmaker(bind=engine)