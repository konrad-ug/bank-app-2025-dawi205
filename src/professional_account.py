from src.account import Account

class ProfessionalAccount(Account): 
    def __init__(self, company_name, NIP):
        super().__init__()
        self.company_name = company_name
        self.balance = 0.0
        self.NIP = NIP if self.is_NIP_valid(NIP) else False
        self.express_fee = 5.0

    def is_NIP_valid(self, NIP):
        if len(NIP) == 10 and NIP.isdigit():
            return True
        return False 
    
    def is_ZUS_paid(self, history):
        if -1775 in history:
            return True
        return False
    
    def take_loan(self, amount):
        if (self.is_ZUS_paid(self.history)) and (self.balance >= amount*2):
            self.balance += amount
            return True
        return False