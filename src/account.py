class Account:
    def __init__(self):
        self.history = []

    def is_transfer_amount_correct(self, amount):
        return self.balance >= amount and amount > 0
        
    def outcoming_transfer(self, amount):
        if self.is_transfer_amount_correct(amount):
            self.balance -= amount
            self.history.append(-amount)
        else:
            "Not enought balance."
    
    def incoming_transfer(self, amount):
        self.balance += amount
        self.history.append(amount)
  
    def outcoming_express_transfer(self, amount):
        if self.is_transfer_amount_correct(amount):
            self.balance -= amount + self.express_fee
            self.history.append(-amount)
            self.history.append(-self.express_fee)
        else:
            "Not enought balance."