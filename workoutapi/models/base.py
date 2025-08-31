from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, UUID, DateTime
from sqlalchemy.sql import func
import uuid

class BaseModel(DeclarativeBase):
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
