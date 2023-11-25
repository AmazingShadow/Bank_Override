from Product import Product
from Main_Bank_VersionX import *
from Bank import *

class SavingsAccount(Account):
    def __init__(self, name, password, money, type):
        super().__init__(name, password , money, type)
        

    # def show_available_balance(self):
    #     print('Balance: ' + str(super().show()))

        