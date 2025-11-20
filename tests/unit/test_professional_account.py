import pytest
from src.account import Account
from src.professional_account import ProfessionalAccount

@pytest.fixture
def create_account():
    def create(company_name="Company", NIP=None):
        return ProfessionalAccount(company_name, NIP)
    return create

@pytest.fixture
def account_with_2k(create_account):
    account = create_account(NIP="1234567890")
    account.balance = 2000
    return account

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

    @pytest.mark.parametrize(
        "history, amount, expected_info, expected_balance",
        [
            ([-1775, 1000, -2000, -5000], 1000, True, 3000),
            ([-1775, 1000, -2000, -5000], 500, True, 2500),
            ([-1800, 1000, -2000, -5000], 500, False, 2000),
            ([-1775, 1000, -2000, -5000], 10000, False, 2000),
        ]
    )
    def test_take_loan(self, account_with_2k, history, amount, expected_info, expected_balance):
        account = account_with_2k
        account.history = history
        print(account.history)
        info = account.take_loan(amount)
        print(account.balance)
        assert info == expected_info
        assert account.balance == expected_balance