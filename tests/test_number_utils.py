

# tests/test_number_utils.py


import pytest
import math
from _pytest.fixtures import FixtureRequest
from typing import Type, Optional, Tuple
from number_analyzer.number_utils import NumberUtils
from number_analyzer.types import NumberLike


@pytest.mark.parametrize('value, expected, error', [

    # even numbers
    (0, True, None),
    (2, True, None),
    (-4, True, None),
    (6, True, None),
    (-8, True, None),
    (10, True, None),

    # odd numbers
    (1, False, None),
    (-3, False, None),
    (5, False, None),
    (-7, False, None),
    (9, False, None),

    # Invaild values
    ('g', None, TypeError),
    (None, None, TypeError),

])
def test_is_even(
    value: NumberLike,
    expected: bool,
    error: Optional[Type[Exception]]
) -> None:

    if error is not None:
        with pytest.raises(error):
            NumberUtils.is_even(value)
    else:
        assert NumberUtils.is_even(value) == expected


@pytest.mark.parametrize('value, expected, error', [

    # prime numbers
    (2, True, None),
    (3, True, None),
    (5, True, None),
    (7, True, None),

    # not prime numbers
    (0, False, None),
    (1, False, None),
    (4, False, None),
    (6, False, None),
    (8, False, None),
    (10, False, None),
    (-1, False, None),
    (-2, False, None),
    (-3, False, None),

    # Invaild values
    ('g', None, TypeError),
    (None, None, TypeError),

])
def test_is_prime(
    value: NumberLike,
    expected: bool,
    error: Optional[Type[Exception]]
) -> None:

    if error is not None:
        with pytest.raises(error):
            NumberUtils.is_prime(value)
    else:
        assert NumberUtils.is_prime(value) == expected


@pytest.mark.parametrize('value, error', [
    (2, None),
    (3, None),
    (5, None),
    (7, None),

    # Invaild values
    ('g', TypeError),
    (None, TypeError),

])
def test_square_root(
    value: NumberLike,
    error: Optional[Type[Exception]],
    sf: int = 2
) -> None:

    if error is not None:
        with pytest.raises(error):
            NumberUtils.square_root(value, sf)

    else:
        result = NumberUtils.square_root(value, sf)
        exact = math.sqrt(value)
        expected_results = (exact, round(exact, sf), round(exact), sf)
        assert result == expected_results
