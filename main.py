from connection.MySQLConnection import MySQLConnection
from manage_data.get_data.GetData import GetData
from manage_data.insert_data.InsertData import InsertData

if __name__ == '__main__':
    connection_pool = MySQLConnection(host="localhost", username="root", password="1234",
                                      database="money")
    connection_pool.connect()
    insert_data = InsertData(connection_pool)
    # insert_data.insert_income()
    # insert_data.insert_bill()
    # insert_data.insert_daily()
    get_data = GetData(connection_pool)

    start_date = "2024-05-01"
    end_date = "2024-05-31"
    daily = get_data.print_get_daily(start_date,end_date)
    bill = get_data.print_get_bill(start_date,end_date)
    loan = get_data.print_get_loan()
    credit = get_data.print_get_credit()
    income = get_data.print_get_income(start_date, end_date)
    get_data.print_summary(credit,loan,bill,daily,income)

