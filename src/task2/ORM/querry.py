from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()


class A(Base):
    __tablename__ = "a"
    id = Column(Integer, primary_key=True)
    name = Column(Text)


class B(Base):
    __tablename__ = "b"
    id = Column(Integer, primary_key=True)
    a_id = Column(Integer, ForeignKey("a.id"))
    data = Column(JSONB)


# Создание подключения к базе данных
engine = create_engine("your_database_url_here")
Session = sessionmaker(bind=engine)
session = Session()

# Запрос с агрегацией
query = (
    select(
        A.id,
        A.name,
        func.sum(func.jsonb_array_length(B.data["list"])).label("total_elements"),
    )
    .join(B, A.id == B.a_id, isouter=True)
    .group_by(A.id, A.name)
)

results = session.execute(query).fetchall()

for row in results:
    print(row)

session.close()
