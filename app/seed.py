from .database import SessionLocal
from .models import User

db = SessionLocal()

users = [
    User(name="Alex", age=25, job="QA Engineer"),
    User(name="John", age=30, job="Backend Developer"),
    User(name="Emma", age=28, job="Designer"),
]

for user in users:
    db.add(user)

db.commit()
db.close()

print("Users added")