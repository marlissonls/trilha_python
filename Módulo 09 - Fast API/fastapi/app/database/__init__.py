from sqlalchemy.orm import sessionmaker
from app.configs import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)