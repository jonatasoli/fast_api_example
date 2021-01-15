from ext.database import Base
from sqlalchemy import Column, String, Integer, Boolean

class Task(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, default="unnamed")
    completed = Column(Boolean, default=False)
