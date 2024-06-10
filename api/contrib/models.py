from uuid import uuid4
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True),default=uuid4, nullable=False)