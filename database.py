from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Настройка базы данных
POSTGRES_URL = "postgresql://username:password@localhost:port/DBname"
engine = create_engine(POSTGRES_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()