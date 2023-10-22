import easy_money
import pytest

@pytest.fixture
def money():
    return easy_money.Account()


def test_when_account_is_created_then_balance_should_be_zero(money):
    assert money.balance == 0


def test_when_money_is_added_then_account_free_amount_should_be_equal_to_added_amount(money):
    expected_amount = easy_money.currency.Money(amount=500)
    money.add(expected_amount)
    assert money.free == expected_amount


def test_when_multiple_amounts_are_added_then_free_amount_should_be_correct(money):
    amount = easy_money.currency.Money(amount=500)
    expected_amount = amount * 3
    for _ in range(3):
        money.add(amount)
    assert money.free == expected_amount
