class CreditCardDAO:
    def __init__(self,connection_pool):
        self.connection_pool = connection_pool

    def insert(self,credit_card):
        query = (f"INSERT INTO credit_card (issuer,total,monthly_return) VALUES ('{credit_card.issuer}',"
                 f"{credit_card.total},{credit_card.monthly_return})")
        self.connection_pool.execute_query(query)

    def update(self,credit_card):
        query = (f"UPDATE credit_card SET issuer='{credit_card.issuer}',total={credit_card.total},"
                 f"monthly_return={credit_card.monthly_return}")
        self.connection_pool.execute_query(query)

    def remove(self,idcredit_card):
        query = f"DELETE FROM credit_card WHERE idcredit_card = {idcredit_card}"
        self.connection_pool.execute_query(query)

    def get(self,idcredit_card):
        query = f"SELECT * FROM credit_card WHERE idcredit_card = {idcredit_card}"
        credit_card = self.connection_pool.execute_query(query)
        return credit_card

    def get_all(self):
        query = f"SELECT * FROM credit_card"
        credit_cards = self.connection_pool.execute_query(query)
        return credit_cards

