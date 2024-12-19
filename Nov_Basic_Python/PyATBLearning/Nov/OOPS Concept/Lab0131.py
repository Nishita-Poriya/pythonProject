class Bank:

    def __init__(self,_account_number,balance):
        self.balance = balance
        self._account_number = _account_number

    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance= self.balance+amount

    def public_function(self):
        self._internal_private_method();

    def show_me_account_number(self,is_auth):
         if is_auth == True:
            print(self._account_number)
         else:
            print("Not allowed")

    def _internal_private_method(self):
        print("Private Method,can be access by only class")

icici= Bank(235245245225,100)
icici.deposit(100)
icici.check_balance()
print(icici.balance)
print(icici._account_number)
icici.show_me_account_number(False)
icici._internal_private_method()

