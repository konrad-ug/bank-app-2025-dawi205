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
        account = Account("John", "Doe", "61121212121", "PROM_XYZ")
        assert account.balance == 50.0
    
    def test_promo_invalid(self):
        account = Account("John", "Doe", "61121212121", "INVALID_XYZ")
        assert account.balance == 0.0

    def test_promo_(self):
        account = Account("John", "Doe", "61121212121", "PROM_XYZ12121212")
        assert account.balance == 0.0

    def test_promo_invalid_format(self):
        account = Account("John", "Doe", "61121212121", "1_234567")
        assert account.balance == 0.0

    def test_promo_invalid_(self):
        account = Account("John", "Doe", "61121212121", "PROM_1234")
        assert account.balance == 0.0

    def test_promo_po_60_2005(self):
        account = Account("John", "Doe", "05221212121", "PROM_XYZ")
        assert account.balance == 50.0

    def test_promo_do_60_1950(self):
        account = Account("John", "Doe", "50121212121", "PROM_XYZ")
        assert account.balance == 0.0

    def test_promo_do_60_1960(self):
        account = Account("John", "Doe", "60121212121", "PROM_XYZ")
        assert account.balance == 0.0
        
    def test_promo_do_60_1961(self):
        account = Account("John", "Doe", "61121212121", "PROM_XYZ")
        assert account.balance == 50.0

    def test_promo_do_60_2160(self):
        account = Account("John", "Doe", "60421212121", "PROM_XYZ")
        assert account.balance == 50.0

    def test_promo_do_60_2060(self):
        account = Account("John", "Doe", "60301212121", "PROM_XYZ")
        assert account.balance == 50.0

    def test_promo_do_60_2199(self):
        account = Account("John", "Doe", "99471212121", "PROM_XYZ")
        assert account.balance == 50.0