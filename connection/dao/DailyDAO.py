from enums.PaymentEnum import PaymentEnum


class DailyDAO:
    def __init__(self,connection_pool):
        self.connection_pool = connection_pool

    def insert(self,daily):
        query = (f"INSERT INTO daily (total,item,date,payment_method) VALUES ({daily.total},"
                 f"'{daily.item}','{daily.date}','{daily.payment_method}')")
        self.connection_pool.execute_query(query)

    def update(self,daily):
        query = (f"UPDATE daily SET total={daily.total},item='{daily.item}',"
                 f"date='{daily.date}',payment_method='{daily.payment_method}'")
        self.connection_pool.execute_query(query)

    def remove(self,iddaily):
        query = f"DELETE FROM daily WHERE iddaily = {iddaily}"
        self.connection_pool.execute_query(query)

    def get(self,iddaily):
        query = f"SELECT * FROM daily WHERE iddaily = {iddaily}"
        daily = self.connection_pool.execute_query(query)
        return daily

    def get_all(self,start_date,end_date):
        query = f"SELECT * FROM daily WHERE date BETWEEN '{start_date}' AND '{end_date}'  AND payment_method = '{PaymentEnum.DEBIT}'"
        dailies = self.connection_pool.execute_query(query)
        return dailies

