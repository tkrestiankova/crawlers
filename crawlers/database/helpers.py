# helpers.py

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from typing import Union

from .. import settings
from ..logger import get_logger

log = get_logger(__name__)


def create_db(url: str) -> tuple:
    """
        Create database engine, session and model base
        for specified database url
    """
    db_engine = sqlalchemy.create_engine(url)
    db_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    )
    base = declarative_base()
    base.query = db_session.query_property()

    return db_engine, db_session, base


def commit_session(session, func_name: str) -> Union[bool, None]:
    try:
        session.commit()
        return True
    except SQLAlchemyError:
        log.error(f"DBError: {func_name} failed.")
        session.rollback()
