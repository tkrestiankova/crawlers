# queries.py

# TODO store to redis and load from redis
# determine id insert or update before using queries

from typing import Union

from .helpers import Session, execute


def create_profiles_table() -> bool:
    query = (
    	"""
    	CREATE TABLE IF NOT EXISTS profiles (
    		name text PRIMARY KEY,
    		phone text,
    		website text
    	);
    	"""
    )
    return execute(query=query)


def update_profile(profile: tuple) -> bool:
    query = (
        """
        UPDATE profiles
        SET phone = ?,
            website = ?
        WHERE name = ?
        """
    )
    return execute(query=query, data=profile)


def instert_profile(profile: tuple) -> bool:
	query = (
		"""
		INSERT INTO profiles(name,phone,website,info_source)
		VALUES(?,?,?,?)
		"""
	)
	return execute(query=query, data=profile)


def get_profiles() -> Union[bool, list]:
	query = (
		"""
		SELECT * from profiles
		"""
	)
	return execute(query=query, fetchall=True)
