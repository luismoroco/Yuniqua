from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__all__ = ["session"]

engine = create_engine("postgresql://yuniqua_admin:root@localhost:5432/yuniqua")
Session = sessionmaker(bind=engine, expire_on_commit=False)


session = Session()
