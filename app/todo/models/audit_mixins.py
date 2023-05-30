from datetime import datetime

from sqlalchemy import Column, DateTime, Integer


class AuditMixin(object):
    date_created = Column(DateTime, default=datetime.utcnow, nullable=True)
    date_updated = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=True,
    )
    created_by_id = Column(Integer)
    updated_by_id = Column(Integer)
