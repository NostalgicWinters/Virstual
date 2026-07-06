from operator import index
from sqlalchemy.engine import default
from session import Base, engine, SessionLocal
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    Table,
    Boolean,
    DateTime,
    Uuid,
)
from sqlalchemy.sql import func
from typing import Generator
from datetime import datetime
import uuid
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = "users"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    avatar_url = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    is_verified = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), default=func.now())
    last_login = Column(DateTime, nullable=True)

    teams = relationship("Teams", back_populates="creator")


class Teams(Base):
    __tablename__ = "teams"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    icon_url = Column(String, nullable=True)
    created_by = Column(Uuid, ForeignKey("users.id"), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), default=func.now())
    is_private = Column(Boolean, default=True)

    creator = relationship("Users", back_populates="teams")


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
