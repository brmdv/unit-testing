import pytest

import original


@pytest.fixture
def get_users():
    return [
        {
            "username": f"John Doe {i}",
            "birthday": f"02/12/19{50+i}",
            "role": "admin" if i % 10 == 0 else "user",
        }
        for i in range(40)
    ]


@pytest.fixture
def get_int_combinations():
    """Fixture to generatate all ints to test add() function."""
    max_r = 10
    return [
        [a, b, c]
        for c in range(1, max_r)
        for b in range(1, max_r)
        for a in range(1, max_r)
    ]


def test_addition(get_int_combinations):
    """Test the addition functions with pytest."""
    assert original.add(get_int_combinations) == sum(get_int_combinations)

