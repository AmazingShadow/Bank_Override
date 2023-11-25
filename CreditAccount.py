from Product import Product
from Main_Bank_VersionX import *
from Bank import *


class CreditAccount(Account):

    def __init__(self, name, password, money, type):
        super().__init__(name, password, money, type)
        self.credit_limit = 0.04
        

    # def show_available_balance(self):
    #     print('Balance: ' + str(super().show()))

    