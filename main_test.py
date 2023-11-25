from Bank import Bank
from Main_Bank_VersionX import Account

ba = Bank()
ba.createAccount('Huy', '123', 1000, 'CASA')
ba.createAccount('Huy', '123', 2000, 'Credit')
ba.createAccount('Hoang', '123', 1000, 'CASA')
ba.createAccount('Hoang', '123', 2000, 'Credit')
# ba.open_account()
ba.withdraw()
ba.show_all_account()
# ba.show()


# a = {}

# print(a.get('Huy') == None)
# a['Huy'] = []
# print(len(a['Huy']))