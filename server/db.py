from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql://yuniqua_admin:root@localhost:5432/yuniqua_editor")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "editor_user"

    editor_user_id = Column(BigInteger(), primary_key=True, autoincrement=True)
    username = Column(String(), nullable=False)
    password = Column(String(), nullable=False)


users = session.query(User).all()

# new_user = User()
# new_user.username = "Lola"
# new_user.password = "root"
#
# session.add(new_user)
# session.commit()

users = session.query(User).all()

for user in users:
    print("USERS-->", user.username)
