import unittest

from typing import List, Dict
from unittest.mock import MagicMock, Mock, patch


class ConnectionDatabaseError(Exception):
    """Raised when the database connection fails."""

    pass


class TestDbError(Exception):
    """Raised when a unit test tries to connect to the database."""

    pass


def connect_to_db(connection_string: str):
    """
    Function that connects to the db.

    We will not give you access to the DB yet. So mock this function if you want to test it.
    """
    print("connection string: ", connection_string)
    if connection_string == "test":
        raise TestDbError("ERROR: YOU FORGOT TO MOCK connect_to_db")
    else:
        raise ConnectionDatabaseError("Can't connect to the database!")


def get_users_list_from_db(connection_string: str) -> List[Dict[str, str]]:
    """
    Function that gets the list of users from the database and returns them as a list of dict.

    Each user is formatted like that: { 'username': 'jonh Doe', 'birthday': '02/12/1985', 'role': 'admin' }
    The unit test should return at least 20 users.
    The unit test should check that all the users have a username, a birthday and a role.
    """
    db = connect_to_db(connection_string)
    users = db.get_user()
    return users


def add(num_1: int, num_2: int, num_3: int) -> int:
    """Add three integers."""
    return num_1 + num_2 + num_3


# unittest parts
class TestAddition(unittest.TestCase):
    """
    This class contains all tests not related to the database stuff, and that
    will be tested using the built-in unittest module.
    """

    def test_many_additions(self):
        """This tests the add() function with all combinations of 3 numbers
        between 1 and 200.

        The code doesn't care for commutativity, so many sums will be tested
        multiple times. The test could obviously be made more efficient when
        taking this into account, but then again, testing 200³ additions of
        positive integers is not the most efficient thing in the first place.
        """

        for a in range(1, 201):
            for b in range(1, 201):
                for c in range(1, 201):
                    self.assertEqual(add(a, b, c), a + b + c)


class TestDatabase(unittest.TestCase):
    """This class contains all tests related to the database."""

    def test_db_connection_is_prohibited(self):
        """Check if databaseconnection is forbidden."""
        self.assertRaises(ConnectionDatabaseError, connect_to_db, "database_test")

    def test_db_connection_is_mock(self):
        """Check if test connection checks for mocking."""
        self.assertRaises(TestDbError, connect_to_db, "test")

    def test_mock_connection(self):
        pass
