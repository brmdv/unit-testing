import unittest

from typing import List, Dict
from unittest.mock import Mock

import original

# # Create database connection Mock
# original.connect_to_db = Mock()

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
                    self.assertEqual(original.add(a, b, c), a + b + c)


class TestDatabase(unittest.TestCase):
    """This class contains all tests related to the database."""

    def test_db_connection_is_prohibited(self):
        """Check if database connection is forbidden."""
        self.assertRaises(
            original.ConnectionDatabaseError, original.connect_to_db, "database_test"
        )

    def test_db_connection_is_mock(self):
        """Check if test connection checks for mocking."""
        self.assertRaises(original.TestDbError, original.connect_to_db, "test")
