from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

import settings


class Database():
    # データベースの基本設定
    def __init__(self):
        # echo=TrueでSQLをログで吐く用にしておく
        self.engine = create_engine(settings.DATABASE_URL, echo=True)
        self.connect_db()

    def connect_db(self):
        Base.metadata.create_all(self.engine)
        session = sessionmaker(self.engine)
        return session()


class Base(DeclarativeBase):
    pass


database = Database()
