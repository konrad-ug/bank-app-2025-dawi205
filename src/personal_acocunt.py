from src.account import Account

class PersonalAccount(Account):
    def __init__(self, first_name, last_name, pesel, promo_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 50.0 if (self.is_promo_code_valid(promo_code) and self.is_year_approved(pesel)) else 0.0
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"

    
    def is_pesel_valid(self, pesel):
        if len(pesel) == 11 and pesel.isdigit():
            return True
        return False
    
    def is_promo_code_valid(self, promo_code):
        if promo_code and promo_code.startswith("PROM_") and len(promo_code) == 8:
            return True
        return False
    
    def is_year_approved(self, pesel):
        year = int(pesel[0:2])
        month = int(pesel[2:4])
       
        if 1 <= month <= 12:
            year += 1900
        elif 21 <= month <= 32:
            year += 2000
        elif 41 <= month <= 52:
            year += 2100
        
        return year > 1960 # zwraca True lub False


    def is_express_transfer_amount_correct(self, amount):
        return self.balance >= amount and amount > 0
    
    def express_outcoming_transfer(self, amount):
        if self.is_express_transfer_amount_correct(amount):
            self.balance -= (amount + 1)
        else:
            "Not enought balance."