from datetime import datetime


class Loan:

    def __init__(self, idloan, amount, issuer, monthly_return, expiration_date, is_credit_card_loan, is_in_frame):
        self.idloan = idloan
        self.amount = amount
        self.issuer = issuer
        self.monthly_return = monthly_return
        self.expiration_date = expiration_date
        self.is_credit_card_loan = is_credit_card_loan
        self.is_in_frame = is_in_frame

    @staticmethod
    def loan(loan):
        now = datetime.now()
        time_left = (loan[4].year - now.year) * 12 + loan[4].month - now.month
        loan_amount = time_left * loan[3]
        return loan_amount

    @staticmethod
    def total_loan_left(loans):
        total = 0
        for loan in loans:
            if not loan[5] or (loan[5] and not loan[6]):
                total += Loan.loan(loan)
        return total

    @staticmethod
    def total_loan_in_cc(loans):
        total = 0
        for loan in loans:
            if loan[5] and loan[6]:
                total += Loan.loan(loan)
        return total

    @staticmethod
    def total_monthly_return(loans):
        total = 0
        for loan in loans:
            if not loan[5]:
                total += loan[3]
        return total

    @staticmethod
    def total_original_loan(loans):
        total = 0
        for loan in loans:
            total += loan[1]
        return total
