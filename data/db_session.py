import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()


__factory = None
db_sess = None
metadata =None
tables = None



def global_init(db_file):
    global __factory, db_sess,metadata,tables

    if __factory:
        db_sess = __factory()
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Получение списка всех таблиц
    tables = metadata.tables
    db_sess = __factory()


def create_session() -> Session:
    global __factory
    if __factory is None:
        return None
    return __factory()