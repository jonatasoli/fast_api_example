# from ext.database import Base
# from sqlalchemy import Column, String, Integer, Boolean
from ext.database import get_engine

db=get_engine()

class Task(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="unnamed")
    completed = db.Column(db.Boolean, default=False)
