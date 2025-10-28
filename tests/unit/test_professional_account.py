from src.account import Account
from src.professional_account import ProfessionalAccount

class TestProfessioinalAccount:
    def test_professional_acocunt_NIP_valid(self):
        account = ProfessionalAccount("Company", "1234567890")
        assert account.NIP == "1234567890"


    def test_professional_acocunt_NIP_too_long(self):
        account = ProfessionalAccount("Company", "123456789000000")
        assert account.NIP == "Invalid"

    def test_professional_acocunt_NIP_not_only_digits(self):
        account = ProfessionalAccount("Company", "123456abcd")
        assert account.NIP == "Invalid"

    def test_professional_acocunt_NIP_too_short(self):
        account = ProfessionalAccount("Company", "123")
        assert account.NIP == "Invalid"
    
    def test_professional_acocunt_incoming_and_outcoming_transfer(self):
        account = ProfessionalAccount("Company", "1234567890")
        account.incoming_transfer(100.0)
        account.outcoming_transfer(60.0)
        assert account.balance == 40.0
    
    def test_professional_acocunt_outcoming_transfer(self):
        account = ProfessionalAccount("Company", "1234567890")
        account.outcoming_transfer(60.0)
        assert account.balance == 0.0

    def test_professional_acocunt_intcoming_transfer(self):
        account = ProfessionalAccount("Company", "1234567890")
        account.incoming_transfer(60.0)
        assert account.balance == 60.0

    def test_express_professional_transfer(self):
        account = ProfessionalAccount("Company", "1234567890")
        account.balance = 50.0
        account.express_outcoming_transfer(50.0)
        assert account.balance == -5.0

    def test_express_professional_transfer_different(self):
        account = ProfessionalAccount("Company", "1234567890")
        account.balance = 52.0
        account.express_outcoming_transfer(50.0)
        assert account.balance == -3.0 

    def test_express_professional_transfer_not_enought(self):
        account = ProfessionalAccount("Company", "1234567890")
        account.balance = 52.0
        account.express_outcoming_transfer(60.0)
        assert account.balance == 52.00 