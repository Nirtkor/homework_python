from HW_1 import line_count
import pytest

lines_tests = [('ABc dbE FRl Ama', '50%'), ('NDp Lka nuR vtE', '25%')]


@pytest.mark.parametrize('line, expect', lines_tests)
def test_line_count(line, expect):
    assert line_count(line) == expect
