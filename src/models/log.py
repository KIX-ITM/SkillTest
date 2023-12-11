from sqlalchemy import Column, Integer, String, Numeric, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.dialects import mysql


class Database():
    def __init__(self):
        # echo=TrueでSQLをログで吐く用にしておく
        self.engine = create_engine('sqlite:///log.sql', echo=True)
        # self.engine = create_engine('mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>', echo=True)
        self.connect_db()

    def connect_db(self):
        Base.metadata.create_all(self.engine)
        session = sessionmaker(self.engine)
        return session()


class Base(DeclarativeBase):
    pass


class AiAnalysisLog(Base):
    __tablename__ = "ai_analysis_log"
    # __table_args__ = {
    #     'mysql_charset': 'utf8',
    #     'mysql_engine': 'InnoDB'
    # }
    id = Column(
        Integer().with_variant(mysql.INTEGER(11), "mysql"),
        primary_key=True, autoincrement=True, nullable=False
    )
    image_path = Column(String(255).with_variant(mysql.VARCHAR(255), "mysql"))
    success = Column(String(255).with_variant(mysql.VARCHAR(255), "mysql"))
    message = Column(String(255).with_variant(mysql.VARCHAR(255), "mysql"))
    img_class = Column('class', Integer().with_variant(mysql.INTEGER(11), "mysql"))
    confidence = Column(Numeric(5, 4).with_variant(mysql.DECIMAL(5, 4), "mysql"))
    request_timestamp = Column(Integer().with_variant(mysql.INTEGER(10), "mysql"))
    response_timestamp = Column(Integer().with_variant(mysql.INTEGER(10), "mysql"))

