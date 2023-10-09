#Multilevel inheritance
class RBI:
    bank_roi=6
    def rbi_guideline(self):
        print("Statutory Restrictions")
        print("Advance against bank's own shares")
        print("Restrictions on holding shares in Companies")
        print('Regulatory Restrictions')

class Bank(RBI):
    bank_name='sbi'
    bank_branch='sbi101'
    bank_ifsc=7890
    
    def __init__(self,n,ac,b):
        self.name=n
        self.account=ac
        self.balance=b
    @staticmethod
    def get_data(s):
        data=int(input(f'Enter data for {s}'))
        return data
    @classmethod
    def display_bank(cls):
        print(cls.bank_name)
        print(cls.bank_ifsc)
        print(cls.bank_branch)
        print(cls.bank_roi)

    def display_obj(self):
        print(Bank.bank_name)
        print(Bank.bank_ifsc)
        print(Bank.bank_branch)
        print(Bank.bank_roi)
        print(self.name)
        print(self.account)
        print(self.balance)
    @classmethod
    def modify_roi(cls):
        newroi=cls.get_data('newroi')
        cls.bank_roi=newroi
        print('Modification Successful for roi')
    def withdraw(self):
        amount=self.get_data('withdraw amount')
        if self.balance>=amount and self.balance>0:
            self.balance-=amount
            print('withdraw successful')
        else:
            print('Low balance')
class Bank_v2(Bank):
    def deposit(self):
        data=self.get_data()
        self.balance+=data
        print('Deposited amount:',data)
        print('Total Balance:',self.balance)
obj1=Bank('Nihal',1234,10000)
obj2=Bank('Tatsat',1235,1000)
obj1.modify_roi()
obj1.withdraw()
obj1.display_obj()
obj2=Bank_v2('Akash',1235,40000)
obj2.withdraw()
obj2.deposit()