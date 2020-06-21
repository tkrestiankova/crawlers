# queries.py

from typing import List

from .. import utils
from . import models
from .helpers import commit_session
from . import CRAWLERS_DB_SESSION


def profiles_get() -> List[dict]:
    """
        Get all yelp profiles
    """
    profiles_alchemy = models.Profiles.query.all()
    return [utils.alchemy_to_dict(p) for p in profiles_alchemy]


def profiles_add(profile: dict) -> None:
    """
        Add new yelp profile
    """
    CRAWLERS_DB_SESSION.add(models.Profiles(
        name=profile["name"],
        phone=profile["phone"],
        website=profile["website"]
    ))
    commit_session(
        session=CRAWLERS_DB_SESSION,
        func_name='profiles_add'
    )


def profiles_update(profile: dict) -> None:
    """
        Update yelp profile
    """
    CRAWLERS_DB_SESSION.merge(
        models.Profiles(
            name=profile["name"],
            phone=profile["phone"],
            website=profile["website"]
        )
    )
    commit_session(
        session=CRAWLERS_DB_SESSION,
        func_name='profiles_update'
    )


def profiles_delete(profile: dict) -> None:
    """
        Delete yelp profile
    """
    existing_profile = models.Profiles.query.filter(
        models.Profiles.name == profile["name"],
    ).first()

    CRAWLERS_DB_SESSION.delete(existing_profile)
    commit_session(
        session=CRAWLERS_DB_SESSION,
        func_name='profiles_delete'
    )
