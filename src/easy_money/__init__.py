from . import currency


class Account:
    """
    This is the primary data representation for Easy Money.

    Funds will be stored here as Money
    """
    def __init__(self):
        self._free = currency.Money(0)

    @property
    def balance(self):
        """
        The total balance of the account, including all free money, goals, and
        in-progress goals. This should be the real money that you have access
        to.
        """
        return 0

    @property
    def free(self):
        return self._free

    def add(self, amount):
        #if not isinstance(amount, currency.Money):
        self._free += amount


def do_it():  # Shia LeBeouf!
    print('actual cannibal')
