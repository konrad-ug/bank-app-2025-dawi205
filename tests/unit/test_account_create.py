from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "12345678901111")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        account.balance += 100.05
        assert account.balance == 100.05
        if (len(account.pesel) == 11):
            assert account.pesel == "12345678901"
        else:
            assert account.pesel == "Invalid"
        