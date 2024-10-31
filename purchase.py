from current_price import current_price
from get_date import get_date


class Purchase:
    def __init__(self, ticker, count) -> None:
        self.ticker = ticker
        self.count = count
        self.date = get_date()  # TODO this
        self.price = current_price(self.ticker)
        self.total = self.price*self.count

    def to_json(self):
        return {'ticker': self.ticker, 'count': self.count, 'date': self.date, 'each': self.price, 'total': self.total}
