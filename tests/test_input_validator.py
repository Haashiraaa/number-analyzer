

# tests/test_input_validator.py

import pytest
import logging
from unittest.mock import MagicMock, patch, create_autospec
from number_analyzer.input_validator import InputHandler
from typing import Optional, cast
from haashi_pkg.utility import Logger


@pytest.fixture
def logger() -> Logger:
    return create_autospec(Logger(logging.INFO), instance=True)


@pytest.mark.parametrize('value, expected', [
    ('q', None),
    ('2', 2),
    ('0.5', 0.5),
])
def test_parse_input_valid(
    value: str,
    expected: Optional[str],
    logger: Logger
) -> None:
    assert InputHandler.parse_input(value, logger) == expected


@patch("number_analyzer.input_validator.su")
def test_parse_input_invalid(su, logger: Logger) -> None:

    for values in ["invalid", ""]:
        result = InputHandler.parse_input(values, logger)

        assert result is None
        cast(MagicMock, logger.warning).assert_called()
