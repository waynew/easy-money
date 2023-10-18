import easy_money
import pytest

@pytest.fixture
def money():
    return easy_money.Money()


def test_this_should_fail(money):
    assert False
