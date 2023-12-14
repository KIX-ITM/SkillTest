from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import func

from src.models.db import Base, database
from src.models.schemas import AiAnalysisLogSchema


class AiAnalysisLog(Base):
    # DBテーブルの設定（sqliteとmysql両方で利用できるよう設定）
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
    request_timestamp = Column(Integer().with_variant(mysql.INTEGER(10, unsigned=True), "mysql"))
    response_timestamp = Column(Integer().with_variant(mysql.INTEGER(10, unsigned=True), "mysql"))

    @staticmethod
    def create(log: AiAnalysisLogSchema):
        # レコードを一行追加、追加したレコードを返す
        session = database.connect_db()
        new_log = AiAnalysisLog(**log)
        session.add(new_log)
        session.commit()
        new_log_id = session.query(func.max(AiAnalysisLog.id)).scalar()
        record = session.query(AiAnalysisLog).get(new_log_id)
        session.close()
        return record
