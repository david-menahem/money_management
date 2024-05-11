class CreditCard:
    credit_cards = []

    def __init__(self, idcredit_card, total, issuer, monthly_return):
        self.idcredit_card = idcredit_card
        self.total = total
        self.issuer = issuer
        self.monthly_return = monthly_return

    @staticmethod
    def total_monthly_return(credit_cards):
        total = 0
        for credit_card in credit_cards:
            total += int(credit_card[3])
        return total

    @staticmethod
    def total_debt(credit_cards):
        total = 0
        for credit_card in credit_cards:
            total += int(credit_card[1])
        return total
