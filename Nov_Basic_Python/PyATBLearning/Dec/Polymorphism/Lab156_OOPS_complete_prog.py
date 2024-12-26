from abc import ABC,abstractmethod

class BankAccount:

    def __init__(self,balance,acc_number):
        self._balance=balance
        self.acc_number = acc_number

class ICICI(BankAccount):

    def withdraw(self):
        print("Yes")

    @abstractmethod
    def loan(self):
        pass

    @staticmethod
    def call_customer_care():
        print("calling")


obj1=ICICI(50000,2352452)
obj1.withdraw()
obj1.call_customer_care()