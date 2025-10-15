from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "12345678901")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        account.balance += 100.05
        assert account.balance == 100.05
        assert account.pesel == "12345678901"
        
    def test_account_pesel_too_long(self):
        account = Account("John", "Doe", "11111111111111111111111")
        assert account.pesel == "Invalid"

    def test_account_pesel_too_short(self):
        account = Account("John", "Doe", "11")
        assert account.pesel == "Invalid"

    def test_account_pesel_not_a_number(self):
        account = Account("John", "Doe", "abc")
        assert account.pesel == "Invalid"

    def test_promo_valid(self):
        account = Account("John", "Doe", "12345678901", "PROM_XYZ")
        assert account.balance == 50.0
    
    def test_promo_invalid(self):
        account = Account("John", "Doe", "12345678901", "INVALID_XYZ")
        assert account.balance == 0.0

    def test_promo_(self):
        account = Account("John", "Doe", "12345678901", "PROM_XYZ12121212")
        assert account.balance == 0.0

    def test_promo_invalid_format(self):
        account = Account("John", "Doe", "12345678901", "1_234567")
        assert account.balance == 0.0

    def test_promo_invalid_(self):
        account = Account("John", "Doe", "12345678901", "PROM_1234")
        assert account.balance == 0.0