from . import error

class Money:
    def __init__(self, amount, *, currency="$"):
        # default currency is dollar. Maybe we want to change this?
        self.currency = currency
        stramount = str(amount)
        if any(txt in stramount for txt in ('.', 'e-')):
            # This may be a silly way to check that there's a decimal
            # point in Money, but honestly it's probably the most
            # reliable way.
            # Had to throw in the `e-` for very smol numbers.
            # TODO: Do we really want to raise an error, or do we want to simply accept and transform? -W. Werner, 2023-10-20
            raise error.MoneyError('asdf')
        self.amount = amount

    def __str__(self):
        if self.currency in ("$",):  # TODO: can add more currency symbols here -W. Werner, 2023-10-20
            return f"{self.currency}{self.amount//100:,}.{self.amount%100:02}"
        else:
            return f"{self.amount//100:,}.{self.amount%100:02} {self.currency}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.amount}, currency={self.currency!r})"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self.currency == other.currency and self.amount == other.amount

    def __mul__(self, other):
        if isinstance(other, int):
            return Money(amount=self.amount*other, currency=self.currency)

    def __truediv__(self, other):
        if not isinstance(other, int):
            raise error.DivisionError(f"Division between Money and {type(other)} is not supported.")
        result, remainder = divmod(self.amount, other)
        if remainder:
            raise error.DivisionError(f"{self.amount} not equally divisible by {other}")
        return Money(amount=result, currency=self.currency)

    def __floordiv__(self, other):
        raise error.DivisionError(f"Division between Money and {type(other)} is not supported.")

    def __divmod__(self, other):
        raise error.DivisionError(f"Division between Money and {type(other)} is not supported.")

    @property
    def dollars(self):
        return self.amount // 100

    @property
    def cents(self):
        return self.amount % 100
