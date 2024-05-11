from enums.PaymentEnum import PaymentEnum


class IncomeDAO:
    def __init__(self,connection_pool):
        self.connection_pool = connection_pool

    def insert(self,income):
        query = (f"INSERT INTO income (name,total,date, payment_method) VALUES ('{income.name}','{income.total}',"
                 f"'{income.date}','{income.payment_method}')")
        self.connection_pool.execute_query(query)

    def update(self,income):
        query = (f"UPDATE income SET name='{income.name}',total={income.total},date='{income.date}',"
                 f"payment_method = '{income.payment_method}"
                 f" WHERE idincome={income.idincome}")
        self.connection_pool.execute_query(query)

    def remove(self, idincome):
        query = f"DELETE FROM income WHERE idincome = {idincome}"
        self.connection_pool.execute_query(query)

    def get(self,idincome):
        query = f"SELECT * FROM income WHERE idincome = {idincome}"
        income = self.connection_pool.execute_query(query)
        return income

    def get_all(self,start_date,end_date):
        query = f"SELECT * FROM income WHERE date BETWEEN '{start_date}' AND '{end_date}' AND payment_method <> '{PaymentEnum.CASH}'"
        incomes = self.connection_pool.execute_query(query)
        return incomes

