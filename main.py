from fastapi import FastAPI, Depends
import uvicorn
from models import Entry
from database import SessionLocal

# Создание приложения FastAPI
app = FastAPI()

# Зависимость для DB сессии
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпойнт для добавления записи
@app.post("/add_entry")
def add_entry(text: str, db_session=Depends(get_db_session)):
    entry = Entry(text=text)
    db_session.add(entry)
    db_session.commit()
    return {"message": "Entry added successfully"}

# Эндпойнт для update записи
@app.put("/update_entry")
def update_entry(id: int, new_text: str, db_session=Depends(get_db_session)):
    entry = db_session.query(Entry).filter(Entry.id == id).first()
    entry.text = new_text
    db_session.commit()
    return {"id": entry.id, "text": entry.text}

# Эндпойнт для удаления записи
@app.delete("/delete_entry")
def delete_entry(id: int, db_session=Depends(get_db_session)):
    entry = db_session.query(Entry).filter(Entry.id == id).first()
    db_session.delete(entry)
    db_session.commit()
    return {"message": "Entry deleted successfully"}

# Эндпойнт для получения записи по id
@app.get("/{id}")
def get_entry_by_id(id: int, db_session=Depends(get_db_session)):
    entry = db_session.query(Entry).filter(Entry.id == id).first()
    return {"id": entry.id, "text": entry.text}

# Эндпойнт для главной страницы
@app.get("/")
def get_entries(db_session=Depends(get_db_session)):
    entries = db_session.query(Entry).all()
    return {"entries": [{"id": entry.id, "text": entry.text} for entry in entries]}

# Запуск приложения
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)