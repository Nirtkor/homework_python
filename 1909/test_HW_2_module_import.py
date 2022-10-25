from HW_2 import date_verify
import pytest

date_tests = [
    (31, 1, 2001, 1),
    (29, 2, 2004, 1),
    (29, 2, 1700, 0),
    (-15, 2, 2007, 0),
    (15, -2, 2007, 0),
    (15, 2, -2007, 1),
    (28, 2, 2005, 1),
]


@pytest.mark.parametrize('day, month, year, expect', date_tests)
def test_date_verify(day, month, year, expect):
    assert date_verify(day, month, year) == expect