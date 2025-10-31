from src.account import Account

class TestAccount:
    def test_history(self):
        account = Account()
        account.balance = 500.0
        account.express_fee = 5.0
        account.outcoming_express_transfer(300)
        assert account.history == [-300, -5.0]

    
    def test_history_instant_not_enough_money(self):
        account = Account()
        account.balance = 500.0
        account.express_fee = 5.0
        account.outcoming_express_transfer(3000)
        assert account.history == []
    
    
    def test_history_outcoming_and_incoming(self):
        account = Account()
        account.balance = 500.0
        account.express_fee = 5.0
        account.outcoming_express_transfer(300)
        account.incoming_transfer(1000)
        account.outcoming_transfer(100)
        assert account.history == [-300.0, -5.0, 1000.0, -100]

    
    def test_history_not_enough_money(self):
        account = Account()
        account.balance = 500.0
        account.express_fee = 1.0
        account.outcoming_transfer(300.0)
        account.incoming_transfer(1000)
        account.outcoming_express_transfer(45000)
        assert account.history == [-300, 1000]