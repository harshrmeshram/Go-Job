from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, gen_uuid


class Resume(Base, TimestampMixin):
    __tablename__ = "resumes"

    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=gen_uuid)
    user_id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    filename: Mapped[str] = mapped_column(String(1024), nullable=False)
    storage_path: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    parsed_text: Mapped[str | None] = mapped_column(Text, nullable=True)

    user = relationship("User", back_populates="resumes")
