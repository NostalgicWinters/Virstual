from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

DatabaseURL = "sqlite:///./Virstual.db"

engine = create_engine(DatabaseURL, connect_args={"check_same_thread": False})

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
