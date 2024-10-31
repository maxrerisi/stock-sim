import json
from SEED_FILE import SEED_CASH
from get_date import get_date


class Portfolio:
    def __init__(self) -> None:
        self.cash_in = SEED_CASH
        self.init_time = get_date()
        self.current_cash = SEED_CASH
        self.max_cash = -1
        self.holdings = {} # TODO This is up next
        self.history = {} # TODO do this
        self.check_max()

    def check_max(self):
        # Update max_cash if current_cash exceeds the previously recorded max_cash
        if self.current_cash > self.max_cash["cash"]:
            self.max_cash = {"cash": self.current_cash, "date": get_date()}

    def to_json(self):
        # Ensure max_cash is up-to-date
        self.check_max()
        # Create a dictionary with the current state of the portfolio
        portfolio_dict = {
            "cash_in": self.cash_in,
            "init_time": self.init_time,
            "current_cash": self.current_cash,
            "max_cash": self.max_cash,
            "holdings": self.holdings,
            "history": self.history
        }
        # Return the dictionary as a JSON string
        return json.dumps(portfolio_dict)