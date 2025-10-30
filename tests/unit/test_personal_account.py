from src.account import Account
from src.personal_acocunt import PersonalAccount

class TestPersonalAccount:
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe", "12345678901")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        account.balance += 100.05
        assert account.balance == 100.05
        assert account.pesel == "12345678901"
        
    def test_express_transfer(self):
        account = PersonalAccount("John", "Doe", "12345678901")
        account.balance = 50.0
        account.outcoming_express_transfer(50.0)
        assert account.balance == -1.0

    def test_express_transfer_too_much(self):
        account = PersonalAccount("John", "Doe", "12345678901")
        account.balance = 50.0
        account.outcoming_express_transfer(60.0)
        assert account.balance == 50.0

    def test_account_pesel_too_long(self):
        account = PersonalAccount("John", "Doe", "11111111111111111111111")
        assert account.pesel == "Invalid"

    def test_account_pesel_too_short(self):
        account = PersonalAccount("John", "Doe", "11")
        assert account.pesel == "Invalid"

    def test_account_pesel_not_a_number(self):
        account = PersonalAccount("John", "Doe", "abc")
        assert account.pesel == "Invalid"

    def test_promo_valid(self):
        account = PersonalAccount("John", "Doe", "61121212121", "PROM_XYZ")
        assert account.balance == 50.0
    
    def test_promo_invalid(self):
        account = PersonalAccount("John", "Doe", "61121212121", "INVALID_XYZ")
        assert account.balance == 0.0

    def test_promo_(self):
        account = PersonalAccount("John", "Doe", "61121212121", "PROM_XYZ12121212")
        assert account.balance == 0.0

    def test_promo_invalid_format(self):
        account = PersonalAccount("John", "Doe", "61121212121", "1_234567")
        assert account.balance == 0.0

    def test_promo_invalid_(self):
        account = PersonalAccount("John", "Doe", "61121212121", "PROM_1234")
        assert account.balance == 0.0

    def test_promo_po_60_2005(self):
        account = PersonalAccount("John", "Doe", "05220000000", "PROM_XYZ")
        assert account.balance == 50.0

    def test_promo_do_60_1950(self):
        account = PersonalAccount("John", "Doe", "50120000000", "PROM_XYZ")
        assert account.balance == 0.0

    def test_promo_do_60_1960(self):
        account = PersonalAccount("John", "Doe", "60120000000", "PROM_XYZ")
        assert account.balance == 0.0
        
    def test_promo_do_60_1961(self):
        account = PersonalAccount("John", "Doe", "61120000000", "PROM_XYZ")
        assert account.balance == 50.0

    def test_promo_do_60_2160(self):
        account = PersonalAccount("John", "Doe", "60420000000", "PROM_XYZ")
        assert account.balance == 50.0

    def test_promo_do_60_2060(self):
        account = PersonalAccount("John", "Doe", "60300000000", "PROM_XYZ")
        assert account.balance == 50.0

    def test_promo_do_60_2199(self):
        account = PersonalAccount("John", "Doe", "99470000000", "PROM_XYZ")
        assert account.balance == 50.0

    def test_money_transfer_outocming(self):
        account = PersonalAccount("John", "Doe", "99470000000", "PROM_XYZ")
        account.outcoming_transfer(50.0)
        assert account.balance == 0.0

    def test_money_transfer_incoming(self):
        account = PersonalAccount("John", "Doe", "99470000000")
        account.balance = 50.0
        account.incoming_transfer(50.0)
        assert account.balance == 100.0

    def test_money_transfer_not_enough_money(self):
        account = PersonalAccount("John", "Doe", "99470000000")
        account.balance = 50.0
        account.outcoming_transfer(100.0)
        assert account.balance == 50.0
    
    def test_money_transfer_incoming_and_outcoming(self):
        account = PersonalAccount("John", "Doe", "99470000000")
        account.balance = 50.0
        account.incoming_transfer(100.0)
        account.outcoming_transfer(50.0)
        assert account.balance == 100.0

    def test_money_transfer_outcoming_and_incoming(self):
        account = PersonalAccount("John", "Doe", "99470000000")
        account.balance = 50.0
        account.outcoming_transfer(10.0)
        account.incoming_transfer(50.0)
        assert account.balance == 90.0
