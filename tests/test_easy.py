import easy_money
import pytest
Money = easy_money.currency.Money

@pytest.fixture
def money():
    return easy_money.Account()


def test_when_account_is_created_then_balance_should_be_zero(money):
    assert money.balance == easy_money.ZERO_DOLLARS


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


def test_when_add_to_non_existent_goal_should_GoalError(money):
    with pytest.raises(easy_money.error.GoalError):
        money.add_to_goal(amount=Money(500), goal="fnord")


def test_creating_multiple_goals_with_the_same_name_should_GoalError(money):
    duplicate_name = "fnord"
    money.create_goal(duplicate_name)
    with pytest.raises(easy_money.error.GoalError, match=f"Duplicate goal {duplicate_name!r}"):
        money.create_goal(duplicate_name)


def test_funds_added_to_goal_should_reflect_in_the_balance_but_not_the_free(money):
    goal_name = "fnord"
    goal_amount = Money(amount=1000)
    free_amount = Money(amount=500)
    money.create_goal(goal_name)
    money.add(free_amount)
    money.add_to_goal(amount=goal_amount, goal=goal_name)

    assert money.balance == Money(amount=1500)
    assert money.free == free_amount
    assert money.goals[goal_name].balance == goal_amount


def test_spending_funds_from_goal_should_reflect_in_balance(money):
    goal_one = "one"
    goal_two = "two"

    five_dollars = Money(amount=500)

    money.create_goal(goal_one)
    money.create_goal(goal_two)

    money.spend_from(goal="free", amount=five_dollars)
    assert money.balance == -five_dollars

    money.add(amount=five_dollars)
    assert money.balance == easy_money.ZERO_DOLLARS

    money.add_to_goal(goal=goal_one, amount=five_dollars)
    money.add_to_goal(goal=goal_two, amount=five_dollars)
    assert money.balance == Money(amount=1000)
    assert money.goals[goal_one].balance == five_dollars
    assert money.goals[goal_two].balance == five_dollars

    money.spend_from(goal=goal_one, amount=five_dollars*2)
    
    assert money.balance == easy_money.ZERO_DOLLARS
