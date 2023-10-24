from . import currency

# TODO: currency type? -W. Werner, 2023-10-24
ZERO_DOLLARS = currency.Money(0)

class Account:
    """
    This is the primary data representation for Easy Money.

    Funds will be stored here as Money
    """
    def __init__(self):
        self._free = Goal(name="free")
        self.goals = {}

    @property
    def balance(self):
        """
        The total balance of the account, including all free money, goals, and
        in-progress goals. This should be the real money that you have access
        to.
        """
        return sum((self.goals[g].balance for g in self.goals), start=ZERO_DOLLARS) + self._free.balance

    @property
    def free(self):
        return self._free.balance

    def add(self, amount):
        #if not isinstance(amount, currency.Money):
        self._free.add(amount=amount)

    def create_goal(self, name):
        if name in self.goals:
            raise error.GoalError(f"Duplicate goal {name!r}")
        self.goals[name] = Goal(name=name)

    def add_to_goal(self, *, amount, goal):
        if goal not in self.goals:
            raise error.GoalError(f"No goal {goal!r}")
        self.goals[goal].add(amount=amount)

    def spend_from(self, *, amount, goal):
        goal = self._free if goal == "free" else self.goals[goal]
        goal.spend(amount=amount)

class Goal:
    """
    A goal is an envelope in the envelope method. But it just represents
    something that you want to save for, like a car, or new tires.
    """
    def __init__(self, *, name):
        self.name = name
        self.money_in = []
        self.money_out = []

    def add(self, *, amount):
        '''
        Add the amount to this goal. If a timestamp is not provided then it will be the current time.
        '''
        if not isinstance(amount, currency.Money):
            raise MoneyError(f"Amount {amount!r} is the wrong type {type(amount)} - should be currency.Money")
        self.money_in.append(amount)

    def spend(self, *, amount):
        self.money_out.append(amount)

    @property
    def balance(self):
        '''
        The total money in this goal. This amount is never negative, though you
        can spend from a goal that you didn't actually add money to. In that case the money will magically be moved from the free pool. It's possible to spend more money than you have in your free pool, in which case you will have spent more money than you have free to spend.
        '''
        # TODO: currency for ZERO_DOLLARS? -W. Werner, 2023-10-24
        return sum(self.money_in, start=ZERO_DOLLARS) - sum(self.money_out, start=ZERO_DOLLARS)


def do_it():  # Shia LeBeouf!
    print('actual cannibal')
