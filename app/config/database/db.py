import urllib.parse as up
from datetime import datetime

import psycopg2
from sqlalchemy import create_engine, func
from sqlalchemy.engine import Engine
from sqlalchemy.orm import (DeclarativeBase, Mapped, Session, mapped_column,
                            sessionmaker)

up.uses_netloc.append("postgres")
# postgres://yqixcbji:9LefPWvqgGw3KdP4oaEWXUb_fc14-atW@jelani.db.elephantsql.com/yqixcbji
url = up.urlparse("yqixcbji:9LefPWvqgGw3KdP4oaEWXUb_fc14-atW@jelani.db.elephantsql.com/yqixcbji")
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)

engine:Engine = create_engine("postgresql+psycopg2://yqixcbji:9LefPWvqgGw3KdP4oaEWXUb_fc14-atW@jelani.db.elephantsql.com/yqixcbji")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TimeStamp:
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now())