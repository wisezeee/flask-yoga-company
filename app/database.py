import os

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session


db = SQLAlchemy()

SqlAlchemyBase = dec.declarative_base()
__factory = None


def global_init():
    global __factory

    if __factory:
        return
    connection_path = f'postgresql+psycopg2://{os.environ.get("POSTGRES_USER")}:' \
                      f'{os.environ.get("POSTGRES_PASSWORD")}' \
                      f'@localhost:38748/{os.environ.get("DB_NAME")}'

    print(f'Происходит подключение к БД {connection_path}!')

    engine = sa.create_engine(connection_path, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)


def create_session():
    global __factory
    return __factory
