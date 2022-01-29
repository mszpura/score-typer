import os

from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, DateTime, Integer, String
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(100)),
    Column("password", String(255)),
    Column("email", String()),
    Column("created_date", DateTime, default=func.now(), nullable=False)
)

# databases query builder
database = Database(DATABASE_URL)
