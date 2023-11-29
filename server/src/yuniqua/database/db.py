from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__all__ = ["DBModule"]

engine = create_engine("postgresql://yuniqua_admin:root@localhost:5432/yuniqua_editor")
Session = sessionmaker(bind=engine)


class DBModule:
    session = None

    def __init__(self):
        self.session = Session()
