from enums.PaymentEnum import PaymentEnum


class BillDAO:
    def __init__(self,connection_pool):
        self.connection_pool = connection_pool

    def insert(self,bill):
        query = (f"INSERT INTO bill (total,company,date, payment_method) VALUES ({bill.total},"
                 f"'{bill.company}','{bill.date}','{bill.payment_method}')")
        self.connection_pool.execute_query(query)

    def update(self,bill):
        query = (f"UPDATE bill SET total={bill.total},company='{bill.company}',"
                 f"date='{bill.date}',payment_method = '{bill.payment_method}")
        self.connection_pool.execute_query(query)

    def remove(self,idbill):
        query = f"DELETE FROM bill WHERE idbill = {idbill}"
        self.connection_pool.execute_query(query)

    def get(self,idbill):
        query = f"SELECT * FROM bill WHERE idbill = {idbill}"
        bill = self.connection_pool.execute_query(query)
        return bill

    def get_all(self,start_date,end_date):
        query = f"SELECT * FROM bill WHERE date BETWEEN '{start_date}' AND '{end_date}' AND payment_method = '{PaymentEnum.DEBIT}'"
        bills = self.connection_pool.execute_query(query)
        return bills

