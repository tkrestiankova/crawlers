# queries.py

from typing import Union

from .helpers import Session, execute


def create_profiles_table() -> bool:
    query = (
    	"""
    	CREATE TABLE IF NOT EXISTS profiles (
    		name text NOT NULL,
    		phone text,
    		website text,
            info_source text NOT NULL,
            primary key (name, info_source)
    	);
    	"""
    )
    return execute(query=query)


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
