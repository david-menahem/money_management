class Bill:

    def __init__(self, idbill, total, company, date, payment_method):
        self.idbill = idbill
        self.total = total
        self.company = company
        self.date = date
        self.payment_method = payment_method

    @staticmethod
    def total_bills(bills):
        total = 0
        for bill in bills:
            total += int(bill[1])
        return total