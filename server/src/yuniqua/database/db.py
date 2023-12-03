from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__all__ = ["DBModule"]

engine = create_engine("postgresql://yuniqua_admin:root@localhost:5432/yuniqua")
Session = sessionmaker(bind=engine, expire_on_commit=False)


class DBModule:
    session = None

    def __init__(self):
        self.session = Session()
