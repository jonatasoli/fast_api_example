from sqlalchemy import Boolean, Column, DateTime, Integer, String

from ext.database import Base

from .audit_mixins import AuditMixin


class Task(Base, AuditMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String, default='unnamed')
    completed = Column(Boolean, default=False)
