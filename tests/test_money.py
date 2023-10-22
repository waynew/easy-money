import pytest
import easy_money.error
import easy_money.currency as cur



def test_money_should_require_an_argument():
    with pytest.raises(TypeError):
        cur.Money()


@pytest.mark.parametrize("amount,expected_dollars,expected_cents",
   [
        (123, 1, 23),
        (321, 3, 21),
        (100, 1, 0),
        (0, 0, 0),
        (11_111_111_111_111_111_111_100, 11_111_111_111_111_111_111_1, 0),
   ]
)
def test_money_should_accept_int_as_dollars_with_cents(amount, expected_dollars, expected_cents):
    # 100 is $1.23
    money = cur.Money(amount)
    assert money.dollars == expected_dollars
    assert money.cents == expected_cents


@pytest.mark.parametrize(
    "amount", [
        123.42,  # simple decimal
        0.0,  # zero!
        0.0000000000000000001,  # smol decimal
        1000000000000.00000000000001,  # large with smol part
        1000000000000.0, # large with zeroth part
        ],
)
def test_money_should_error_if_fractional_parts_are_provided(amount):
    with pytest.raises(easy_money.error.MoneyError):
        cur.Money(amount)


@pytest.mark.parametrize(
    "expected_str, amount, currency",[
        ("$1.00", 100, "$"),
        ("1.00 USD", 100, "USD"),
        ("$0.01", 1, "$"),
        ("0.02 USD", 2, "USD"),
        ("$1.01", 101, "$"),
        ("1.23 USD", 123, "USD"),
        ("3.21 USD", 321, "USD"),
        # TODO: Add other currencies here -W. Werner, 2023-10-20
])
def test_str_should_provide_correct_str_with_amount(expected_str, amount, currency):
    assert str(cur.Money(amount, currency=currency)) == expected_str


def test_repr_should_be_repr():
    money = cur.Money(100)
    assert repr(money) == "Money(100, currency='$')"
    Money = cur.Money
    assert money == eval(repr(money))

@pytest.mark.parametrize(
    "currencies", [
        ("$", "USD"),  # TODO: these could map but we don't have it yet -W. Werner, 2023-10-20
        ("$", "%"),
        ("USD", "GBP"),
        ("YEN", "GBP"),
    ]
)
def test_money_equality_should_fail_if_currency_does_not_match(currencies):
    # TODO: theoretically we can define conversions but that's for a long time from now -W. Werner, 2023-10-20
    amount = 10
    assert cur.Money(amount, currency=currencies[0]) != cur.Money(amount, currency=currencies[1])


@pytest.mark.parametrize(
    "amount, currency", [
        (0, "USD"),
        (-100, "USD"),
        (501, "USD"),
        (-100042134, "USD"),
        (1000, "$"),
        (1020, "¥"),
        (1003, "£"),
        (1000, "GBP"),
        (1400, "USD"),
        (1000, "USD"),
        (1090, "USD"),
        (1000, "USD"),
    ]
)
def test_money_should_be_equal_with_same_currencies_and_amount(amount, currency):
    assert cur.Money(amount, currency=currency) == cur.Money(amount, currency=currency)


@pytest.mark.parametrize(
    "amount, currency", [
        (0, "USD"),
        (-100, "USD"),
        (501, "USD"),
        (-100042134, "USD"),
        (1000, "$"),
        (1020, "¥"),
        (1003, "£"),
        (1000, "GBP"),
        (1400, "USD"),
        (1000, "USD"),
        (1090, "USD"),
        (1000, "USD"),
    ]
)
def test_money_should_be_not_equal_with_same_currencies_and_different_amount(amount, currency):
    assert cur.Money(amount, currency=currency) != cur.Money(amount+1, currency=currency)
    assert cur.Money(amount, currency=currency) != cur.Money(amount-1, currency=currency)


@pytest.mark.parametrize(
    "amount, multiplier, expected_amount", [
        (100, 0, 0),
        (100, 1, 100),
        (100, 2, 200),
])
def test_money_should_be_multipliable_by_amount_and_return_money(amount, multiplier, expected_amount):
    assert cur.Money(amount) * multiplier == cur.Money(expected_amount)

@pytest.mark.parametrize(
    "amount, currency", [
        (100, "USD"),
        (100, "GBP"),
        (100, "$"),
])
def test_multiplying_money_should_keep_currency(amount, currency):
    expected_amount = amount * 2
    assert cur.Money(amount, currency=currency) * 2 == cur.Money(expected_amount, currency=currency)


@pytest.mark.parametrize(
    "divisor", [
        1.0,
        0.0,
        92.3,
    ]
)
def test_division_should_fail_for_non_int_types(divisor):
    money = cur.Money(40)
    # True division
    with pytest.raises(easy_money.error.DivisionError):
        money / divisor

    # floor aka classic division
    with pytest.raises(easy_money.error.DivisionError):
        money // divisor

    # and why not?
    with pytest.raises(easy_money.error.DivisionError):
        divmod(money, divisor)


@pytest.mark.parametrize(
    "amount, divisor", [
        (1, 2),  # We can't have a ha'penny
        (100, 3),  # Irrational cents are irrational
])
def test_division_that_has_a_remainder_should_error(amount, divisor):
    # TODO: I'm not 100% positive about this behavior. Should this be accurate in *all* cases? -W. Werner, 2023-10-22
    with pytest.raises(easy_money.error.DivisionError):
        cur.Money(amount) / divisor


@pytest.mark.parametrize(
    "amount, divisor, expected_amount", [
        (2,1,2),
        (0,2,0),  # zero divided by anything is zero!
        (100,2,50),  # zero divided by anything is zero!
        (33,3,11),
])
def test_division_with_accurate_divisor_should_produce_money_bits(amount, divisor, expected_amount):
    money = cur.Money(amount)
    expected_result = cur.Money(expected_amount)
    result = money / divisor
    assert result == expected_result
