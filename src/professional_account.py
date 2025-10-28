from src.account import Account

class ProfessionalAccount(Account): 
    def __init__(self, company_name, NIP):
        self.company_name = company_name
        self.balance = 0.0
        self.NIP = NIP if self.is_NIP_valid(NIP) else "Invalid"

    def is_NIP_valid(self, NIP):
        if len(NIP) == 10 and NIP.isdigit():
            return True
        return False
    def is_transfer_amount_correct(self, amount):
        return self.balance >= amount and amount > 0
        
    def outcoming_transfer(self, amount):
        if self.is_transfer_amount_correct(amount):
            self.balance -= amount
        else:
            print("Not enought balance.")
    
    def incoming_transfer(self, amount):
        self.balance += amount
    
    def express_outcoming_transfer(self, amount):
        if self.is_transfer_amount_correct(amount):
            self.balance -= (amount + 5)
        else:
            "Not enought balance."
