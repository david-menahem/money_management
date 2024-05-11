class Daily:
    def __init__(self, iddaily, total, item, date, payment_method):
        self.iddaily = iddaily
        self.total = total
        self.item = item
        self.date = date
        self.payment_method = payment_method

    @staticmethod
    def total_item_cost(items):
        total = 0
        for item in items:
            total += int(item[1])
        return total
