'''
BANK MANAGEMENT
Through the terminal interface the user can do some common bank operations as:
* open and close a bank account
* view the balance
* deposit and withdraw
* check the bank account infos
* (admin) check the user accounts
Made by Alessandro Silvestri - 2023 <alessandro.silvestri.work@gmail.com>
'''

from Main_Bank_VersionX import Account
from SavingsAccount import SavingsAccount
from CreditAccount import CreditAccount

class Bank():
    def __init__(self):
        self.accountsDict = {}
    # {account1: [SavingsAccount , CreditAccount], }

    def createAccount(self, name, password, money, type):
        '''method that will be used in open_account method'''
        if self.accountsDict.get(name) == None:
            self.accountsDict[name] = []

        if (type == 'CASA'):
            oAccount = SavingsAccount(name, password, money, type)
        else:
            oAccount = CreditAccount(name, password, money, type)
        
        if len(self.accountsDict[name]) == 0:
            self.accountsDict[name].append(oAccount)
        else:
            self.accountsDict[name].append(oAccount)
        
    
    def open_account(self):
        '''creating a new account with interaction'''
        print("\n*** Open Account ***")

        # input
        name = input("Insert your name: ")
        pw = input("Insert your pw: ")
        choose = input('What type of account do you want to open?\n1. Saving account\n2. Credit account')
        if choose == '1':
            type = 'CASE'
        else:
            type = 'Credit'

        first_amount = int(input("Insert amount £: "))
        self.createAccount(name=name, password=pw, money=first_amount, type=type)

    def closeAccount(self):
        '''eliminate an account and check if there are funds'''
        print("\n*** Close Account ***")
        type = ''
        account_name = input("Insert name of account: ")
        choose = int(input('What type of account do you want to delete\n1. CASA\n2. Credit\nYour choose: '))

        if choose == 1:
            type = 'CASA'
        else:
            type = 'Credit'

        pw = input("Insert your password: ")

        for i in range(len(self.accountsDict.get(account_name))):
            if self.accountsDict.get(account_name)[i].type == type:
                if self.accountsDict.get(account_name)[i].password == pw:
                    print(f"pw ok!")
                    balance = self.accountsDict.get(account_name)[i].balance
                    if balance > 0:
                        print(f"You had {balance} in your bank account wich they will return to you")
                    self.accountsDict.get(account_name).pop(i)
                    break
                else:
                    print("wrong password\nprogram ended")
                    break

    def balance(self):
        '''it shows the balance of a single account'''
        print("\n*** Balance ***")
        account_name = input("Insert name of account: ")

        choose = int(input('What type of account do you want to get balance\n1. CASA\n2. Credit\nYour choose: '))

        if choose == 1:
            type = 'CASA'
        else:
            type = 'Credit'
        pw = input("Insert your password: ")

        for i in range(len(self.accountsDict.get(account_name))):
            if self.accountsDict.get(account_name)[i].type == type:
                if self.accountsDict.get(account_name)[i].password == pw:
                    print(f"pw ok!")
                    balance = self.accountsDict.get(account_name)[i].balance
                    print('Balance: ' + str(balance))
                    break
                else:
                    print("wrong password\nprogram ended")
                    break

    def deposit(self):
        '''deposit in the account'''
        print("\n*** Deposit ***")

        account_name = input("Insert the account name: ")
        choose = int(input('What type of account do you want to get balance\n1. CASA\n2. Credit\nYour choose: '))

        if choose == 1:
            type = 'CASA'
        else:
            type = 'Credit'

        pw = input("Insert your password: ")
        for i in range(len(self.accountsDict.get(account_name))):
            if self.accountsDict.get(account_name)[i].type == type:
                if self.accountsDict.get(account_name)[i].password == pw:
                    print(f"pw ok!")
                    money = int(input('insert the amount you want deposit: '))
                    self.accountsDict.get(account_name)[i].balance +=  money
                    print(f"deposit of {money} done!")
                    break
                else:
                    print("wrong password\nprogram ended")
                    break

    def withdraw(self):
        '''withdraw '''
        print("\n*** Withdraw ***")
        account_name = input("Insert the account name: ")
        choose = int(input('What type of account do you want to get balance\n1. CASA\n2. Credit\nYour choose: '))

        if choose == 1:
            type = 'CASA'
        else:
            type = 'Credit'

        pw = input("Insert your password: ")
        for i in range(len(self.accountsDict.get(account_name))):
            if self.accountsDict.get(account_name)[i].type == type:
                if self.accountsDict.get(account_name)[i].password == pw:
                    print(f"pw ok!")
                    money = int(input('insert the withdraw amount: '))
                    self.accountsDict.get(account_name)[i].balance -=  money
                    print(f"withdraw of {money} done!")
                    break
                else:
                    print("wrong password\nprogram ended")
                    break
    
    def show(self):
        '''show the info of a specific account: num, name, funds'''
        print("\n*** Show info account ***")
        account_name = input("Insert the account name: ")
        choose = int(input('What type of account do you want to get balance\n1. CASA\n2. Credit\nYour choose: '))

        if choose == 1:
            type = 'CASA'
        else:
            type = 'Credit'

        pw = input("Insert your password: ")
        for i in range(len(self.accountsDict.get(account_name))):
            if self.accountsDict.get(account_name)[i].type == type:
                if self.accountsDict.get(account_name)[i].password == pw:
                    print(f"pw ok!")
                    type_acc = self.accountsDict.get(account_name)[i].type
                    balance = self.accountsDict.get(account_name)[i].balance
                    
                    print(f"Type account N: {type_acc} Balance: {balance}")
                    break
                else:
                    print("wrong password\nprogram ended")
                    break

    def show_all_account(self):
        '''for debug/admin'''
        print("\n*** Accounts list ***")
        if len(self.accountsDict) == 0:
            print("<empty>")
        else:
            for key, value in self.accountsDict.items():
                str = ''
                for i in range(len(value)):
                    if i == 0:
                       str += f'name: {key}, [type: {value[i].type}, balance: {value[i].balance}] | '
                    elif i == 1:
                       str += f'[type: {value[i].type}, balance: {value[i].balance}]'
                print(str)
                       
