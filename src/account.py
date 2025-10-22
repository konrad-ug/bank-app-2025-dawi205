class Account:
    def __init__(self, first_name, last_name, pesel, promo_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 50.0 if (self.is_promo_code_valid(promo_code) and self.is_year_approved(pesel)) else 0.0
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"

    def is_transfer_amount_correct(self, amount):
        return self.balance >= amount and amount > 0
        
    def outcoming_transfer(self, amount):
        if self.is_transfer_amount_correct(amount):
            self.balance -= amount
        else:
            "Not enought balance."
    
    def incoming_transfer(self, amount):
        self.balance += amount

    def is_express_transfer_amount_correct(self, amount):
        return self.balance >= amount and amount > 0
    
    def express_outcoming_transfer(self, amount):
        if self.is_express_transfer_amount_correct(amount):
            self.balance -= (amount + 1)
        else:
            "Not enought balance."