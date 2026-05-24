from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from .models import Base, User
from .schemas import UserResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    db: Session = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()

    db.close()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user