import pytest
from src.account import Account
from src.professional_account import ProfessionalAccount

@pytest.fixture
def create_account():
    def create(company_name="Company", NIP=None):
        return ProfessionalAccount(company_name, NIP)
    return create
        
class TestProfessioinalAccount:

    @pytest.mark.parametrize(
            "NIP, expected_info",
            [
                ("1234567890", "1234567890"),
                ("123456789000000", False),
                ("123456abcd", False),
                ("123", False),
            ]
    )
    def test_NIP(self, create_account, NIP, expected_info):
        account = create_account(NIP=NIP)
        assert account.NIP == expected_info