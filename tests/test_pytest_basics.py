import pytest

pytestmark = pytest.mark.learning


def test_addition() -> None:
    actual_result = 2 + 2
    expected_result = 4
    assert actual_result == expected_result
