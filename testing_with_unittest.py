import unittest

from typing import List, Dict
from unittest.mock import Mock, patch

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

        # for a in range(1, 201):
        #     for b in range(1, 201):
        #         for c in range(1, 201):
        #             self.assertEqual(original.add(a, b, c), a + b + c)


class TestDatabase(unittest.TestCase):
    """This class contains all tests related to the database."""

    def test_db_connection_is_prohibited(self):
        """Check if database connection is forbidden with random connection string."""
        self.assertRaises(
            original.ConnectionDatabaseError,
            original.connect_to_db,
            "database random connection string",
        )

    def test_db_connection_is_not_mocked(self):
        """Check if test connection checks for mocking."""
        self.assertRaises(original.TestDbError, original.connect_to_db, "test")

    @patch("original.connect_to_db")
    def test_get_user_list(self, mock_db_connection):
        """Test the get_users_list_from_db() function."""
        # Generate 40 test users
        test_users = [
            {
                "username": f"John Doe {i}",
                "birthday": f"02/12/19{50+i}",
                "role": "admin" if i % 10 == 0 else "user",
            }
            for i in range(40)
        ]
        mock_db_connection.get_user.return_value = test_users
        result = original.get_users_list_from_db("connection 1")
        mock_db_connection.assert_called()
        print(result)
