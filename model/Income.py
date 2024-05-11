class Income:

    def __init__(self,idincome, name, total, date, payment_method):
        self.idincome = idincome
        self.name = name
        self.total = total
        self.date = date
        self.payment_method = payment_method

    @staticmethod
    def total_income(incomes):
        total = 0
        for income in incomes:
            total += int(income[2])

        return total
