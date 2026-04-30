import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Uses SQLite for the Sandbox, but can be swapped to Postgres via Env Var
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///practice.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
