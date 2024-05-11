from connection.dao.BankDAO import BankDAO
from connection.dao.BillDAO import BillDAO
from connection.dao.CreditCardDAO import CreditCardDAO
from connection.dao.DailyDAO import DailyDAO
from connection.dao.IncomeDAO import IncomeDAO
from connection.dao.LoanDAO import LoanDAO
from enums.BillEnum import BillEnum
from enums.CreditCardEnum import CreditCardEnum
from enums.IncomeEnum import IncomeEnum
from enums.LoanEum import LoanEnum
from enums.PaymentEnum import PaymentEnum
from model.BankAccount import BankAccount
from model.Income import Income
from model.expense.Bill import Bill
from model.expense.CreditCard import CreditCard
from model.expense.Daily import Daily
from model.expense.Loan import Loan


class InsertData:
    def __init__(self,connection_pool):
        self.incomeDAO = IncomeDAO(connection_pool)
        self.loanDAO = LoanDAO(connection_pool)
        self.credit_cardDAO = CreditCardDAO(connection_pool)
        self.billDAO = BillDAO(connection_pool)
        self.dailyDAO = DailyDAO(connection_pool)
        self.bankDAO = BankDAO(connection_pool)

    # def insert_bank(self):
    #     balance = BankAccount(None,"Bank_Leumi",,"2024-06-01")
    #     self.bankDAO.insert( balance)
    #     balance = BankAccount(None,"pepper",,"2024-06-01")
    #     self.bankDAO.insert(balance)

    def insert_daily(self):
        expense = Daily(None, 55, "coffe", "2024-05-08", PaymentEnum.CASH)
        self.dailyDAO.insert(expense)
        expense = Daily(None, 195, "jewelery", "2024-05-08", PaymentEnum.CASH)
        self.dailyDAO.insert(expense)
        expense = Daily(None, 70, "cigarettes", "2024-05-09", PaymentEnum.CASH)
        self.dailyDAO.insert(expense)
        expense = Daily(None, 500, "elad loan", "2024-05-10", PaymentEnum.DEBIT_CARD)
        self.dailyDAO.insert(expense)

    def insert_bill(self):
        # bill = Bill(None,90,BillEnum.AQUA,"2024-05-10")
        # self.billDAO.insert(bill)
        # bill = Bill(None,60,BillEnum.MACCABI,"2024-05-05")
        # self.billDAO.insert(bill)
        # bill = Bill(None,33,BillEnum.NETFLIX,"2024-05-21")
        # self.billDAO.insert(bill)
        # bill = Bill(None,84,BillEnum.CLALIT,"2024-05-21")
        # self.billDAO.insert(bill)
        # bill = Bill(None,36,BillEnum.PANGO,"2024-05-26")
        # self.billDAO.insert(bill)
        # bill = Bill(None,163,BillEnum.PARTNER,"2024-05-28")
        # self.billDAO.insert(bill)
        bill = Bill(None,5300,BillEnum.RENT,"2024-05-15")
        self.billDAO.insert(bill)

    # def insert_loan(self):
    #     loan = Loan(None, 15000, LoanEnum.LEUMI, 1000, "2025-12-10", 0, 0)
    #     self.loanDAO.insert(loan)

    # def insert_credit(self):
    #     # credit_card = CreditCard(None, 3000, CreditCardEnum.CAL, 600)
    #     # self.credit_cardDAO.insert(credit_card)
    #
    def insert_income(self):
        # income = Income(None,IncomeEnum.HOUSE_RENT_HELP,1270,"2024-05-06")
        # self.incomeDAO.insert(income)
        # income = Income(None,IncomeEnum.BITUACH_LEUMI_DAVID,4175,"2024-05-28")
        # self.incomeDAO.insert(income)
        # income = Income(None,IncomeEnum.BITUACH_LEUMI_YAEL,4291,"2024-05-28")
        # self.incomeDAO.insert(income)
        # income = Income(None,IncomeEnum.BITUACH_LEUMI_YAEL,4291,"2024-05-28")
        # self.incomeDAO.insert(income)
        income = Income(None,IncomeEnum.MARKET_PLACE,150,"2024-05-10")
        self.incomeDAO.insert(income)
        income = Income(None,IncomeEnum.MARKET_PLACE,50,"2024-05-10")
        self.incomeDAO.insert(income)
        income = Income(None,IncomeEnum.MARKET_PLACE,50,"2024-05-15")
        self.incomeDAO.insert(income)
        income = Income(None,IncomeEnum.SALARY,4487,"2024-05-10")
        self.incomeDAO.insert(income)
