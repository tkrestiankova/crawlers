# models.py

from sqlalchemy import Column, String

from . import CRAWLERS_BASE


class Profiles(CRAWLERS_BASE):
    __tablename__ = 'profiles'

    name = Column(String(), primary_key=True)
    phone = Column(String())
    website = Column(String())
