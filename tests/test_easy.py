import easy_money
import pytest

@pytest.fixture
def money():
    return easy_money.Account()


def test_when_account_is_created_then_balance_should_be_zero(money):
    assert money.balance == 0
