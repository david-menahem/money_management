class BankDAO:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool

    def insert(self, bank):
        query = ("INSERT INTO bank (name, balance, date) VALUES "
                 f"'{bank.name}',{bank.balance},'{bank.date}'")
        self.connection_pool.execute_query(query)

    def update(self, bank):
        query = (f"UPDATE bank SET name = '{bank.name}', balance = {bank.balance}, date = '{bank.date}'"
                 f"WHERE idbank = {bank.idbank}")
        self.connection_pool.execute_query(query)

    def remove(self, id):
        query = f"DELETE FROM bank WHERE idbank = {id}"
        self.connection_pool.execute_query(query)

    def get_balance(self, id):
        query = f"SELECT balnce FROM bank WHERE idbank = {id}"
        balance = self.connection_pool.execute_query(query)
        return balance

    def get_last_balance(self,name):
        query = (f"SELECT balance FROM bank WHERE idbank = "
                 f"(SELECT max(idbank) WHERE name = {name}")
        last_balance = self.connection_pool.execute_query(query)
        return last_balance
