from connection.dao.BillDAO import BillDAO
from connection.dao.CreditCardDAO import CreditCardDAO
from connection.dao.DailyDAO import DailyDAO
from connection.dao.IncomeDAO import IncomeDAO
from connection.dao.LoanDAO import LoanDAO
from model.Income import Income
from model.expense.Bill import Bill
from model.expense.CreditCard import CreditCard
from model.expense.Daily import Daily
from model.expense.Loan import Loan


class GetData:
    def __init__(self,connection_pool):
        self.incomeDAO = IncomeDAO(connection_pool)
        self.loanDAO = LoanDAO(connection_pool)
        self.credit_cardDAO = CreditCardDAO(connection_pool)
        self.billDAO = BillDAO(connection_pool)
        self.dailyDAO = DailyDAO(connection_pool)

    def print_get_income(self,start_date, end_date):
        data = self.incomeDAO.get_all(start_date, end_date)
        total_monthly_income = Income.total_income(data)
        print(f"The total income is: {total_monthly_income}")
        return total_monthly_income

    def print_get_loan(self):
        loans = self.loanDAO.get_all()
        total_original_loan = Loan.total_original_loan(loans)
        total_loan_left = Loan.total_loan_left(loans)
        print(f"The total loan left to pay is: {total_loan_left} from the original loan of: {total_original_loan}")
        total_loan_in_cc = Loan.total_loan_in_cc(loans)
        total_loans_monthly_return = Loan.total_monthly_return(loans)
        print(f"The total monthly return of the loans is: {total_loans_monthly_return}")
        return total_loan_in_cc,total_loans_monthly_return,total_loan_left

    def print_get_credit(self):
        credit_cards = self.credit_cardDAO.get_all()
        total_credit_cards = CreditCard.total_debt(credit_cards)
        total_credit_cards_monthly_return = CreditCard.total_monthly_return(credit_cards)
        return total_credit_cards,total_credit_cards_monthly_return

    def print_get_bill(self,start_date, end_date):
        monthly_bills = self.billDAO.get_all(start_date, end_date)
        total_monthly_bill = Bill.total_bills(monthly_bills)
        print(f"The monthly bills for march is {total_monthly_bill}")
        return total_monthly_bill

    def print_get_daily(self,start_date,end_date):
        daily_expenses_month = self.dailyDAO.get_all(start_date, end_date)
        total_monthly_expense = Daily.total_item_cost(daily_expenses_month)
        print(f"The total monthly expenses for march is {total_monthly_expense}")
        return total_monthly_expense

    def print_summary(self,credit,loan,bill,daily,income):
        print(f"The total credit card debt is: {credit[0] + loan[0]}\n"
              f"The monthly return is: {credit[1]}")
        print()
        total_monthly_return = loan[1] + credit[1]
        print(f"The total debt is {loan[2] + credit[0] + loan[0]}\n"
              f"The total monthly return is {total_monthly_return}")

        total_expense = total_monthly_return + bill + daily
        print(f"The monthly balance is {income - total_expense}")