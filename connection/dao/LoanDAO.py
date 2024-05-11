class LoanDAO:
    def __init__(self,connection_pool):
        self.connection_pool = connection_pool

    def insert(self,loan):
        query = (f"INSERT INTO loan (issuer,amount,monthly_return,expiration_date,is_credit_card_loan,is_in_frame) VALUES ('{loan.issuer}',"
                 f"{loan.amount},{loan.monthly_return},'{loan.expiration_date}','{loan.is_credit_card_loan}','{loan.is_in_frame}')")
        self.connection_pool.execute_query(query)
    def update(self,loan):
        query = (f"UPDATE loan SET issuer='{loan.issuer}',amount={loan.amount},"
                 f"monthly_return={loan.monthly_return},expiration_date='{loan.expiration_date}'"
                 f",is_credit_card_loan'='{loan.is_credit_card_loan}',is_in_frame='{loan.is_in_frame}'"
                 f" WHERE idloan={loan.idloan}")
        self.connection_pool.execute_query(query)

    def remove(self,idloan):
        query = f"DELETE FROM loan WHERE idloan = {idloan}"
        self.connection_pool.execute_query(query)

    def get(self,idloan):
        query = f"SELECT * FROM loan WHERE idloan = {idloan}"
        loan = self.connection_pool.execute_query(query)
        return loan

    def get_all(self):
        query = f"SELECT * FROM loan"
        loans = self.connection_pool.execute_query(query)
        return loans

