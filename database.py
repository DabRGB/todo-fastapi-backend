import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path

# Load .env from project root (2 levels up from this file)
env_path = Path(__file__).resolve().parent.parent / ".env"
print(f"Looking for .env at: {env_path}")  # Debug
load_dotenv(env_path)

# Get connection string
DB_URL = "postgresql+psycopg2://todolist_django_render_pqsu_user:0WNrhPMDSLxLPkX65wUXUwH266NARXx5@dpg-cvnu4mruibrs73aeldg0-a.singapore-postgres.render.com/todolist_django_render_pqsu?sslmode=require"

# Debug output
print(f"Database URL loaded: {DB_URL}")

if not DB_URL:
    raise ValueError("DATABASE_URL not found in .env file")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()