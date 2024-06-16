from database import Base
from sqlalchemy import Column, Integer, String

# Определение модели
class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)