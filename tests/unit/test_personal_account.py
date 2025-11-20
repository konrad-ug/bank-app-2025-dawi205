import pytest
from src.personal_acocunt import PersonalAccount

@pytest.fixture
def create_account():
    def create(first="John", last="Doe", pesel="61121212121", promo=None):
        return PersonalAccount(first, last, pesel, promo)
    return create

@pytest.fixture
def account_with_50_balance(create_account):
    account = create_account()
    account.balance = 50
    return account

class TestPersonalAccount:
    def test_account_creation(self, create_account):
        account = create_account()
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        account.balance += 100.99
        assert account.balance == 100.99
        assert account.pesel == "61121212121"

    @pytest.mark.parametrize(
        "pesel, validation",
        [
            ("11111111111111111111111", "Invalid"),
            ("11", "Invalid"), 
            ("abc", "Invalid"),
            ("61121212121", "61121212121")
        ]
    )
    def test_pesel(self, create_account, pesel, validation):
        account = create_account(pesel=pesel)
        assert account.pesel == validation

    @pytest.mark.parametrize(
            "promo, balance",
            [
                ("PROM_XYZ", 50),
                ("INVALID_XYZ", 0),
                ("PROM_XYZ12121212", 0),
                ("1_234567", 0),
                ("PROM_1234", 0)
            ]
    )
    def test_promo(self, create_account, promo, balance):
        account = create_account(promo=promo)
        assert account.balance == balance

    @pytest.mark.parametrize(
            "pesel, balance",
            [
                ("05220000000", 50),
                ("50120000000", 0),
                ("60120000000", 0),
                ("61121212121", 50), 
                ("60420000000", 50),
                ("60300000000", 50),
                ("99470000000", 50)
            ]
    )
    def test_promo_with_age_restriction(self, create_account, pesel, balance):
        account = create_account(pesel=pesel, promo="PROM_XYZ")
        assert account.balance == balance

    @pytest.mark.parametrize(
            "amount, expected_balance, expected_info",
            [
                (50, -1, True), # True/False odpowiada za powodzenie transakcji
                (60, 50, False),
                (22, 27, True),
                (1, 48, True)
            ]
    )
    def test_outcoming_express_transfer(self, account_with_50_balance, amount, expected_balance, expected_info):
        account = account_with_50_balance
        info = account.outcoming_express_transfer(amount)
        assert account.balance == expected_balance
        assert info == expected_info

    @pytest.mark.parametrize(
            "amount, expected_balance, expected_info",
            [
                (50, 0, True),
                (100, 50, False),
                (30, 20, True),
                (10, 40, True)
            ]
    )
    def test_outcoming_transfers(self, account_with_50_balance, amount, expected_balance, expected_info):
        account = account_with_50_balance
        info = account.outcoming_transfer(amount)
        assert account.balance == expected_balance
        assert info == expected_info

    @pytest.mark.parametrize(
            "amount, expected_balance",
            [
                (50, 50),
                (100, 100),
                (1234, 1234),
                (10.5, 10.5)
            ]
    )
    def test_incoming_transfer(self, create_account, amount, expected_balance):
        account = create_account()
        account.incoming_transfer(amount)
        assert account.balance == expected_balance

    @pytest.mark.parametrize(
            "history, amount, expected_info",
            [
                ([20, -100000, 10, 10, 10], 1000000000, True),
                ([20, -10, 10, -10, 10], 20, True),
                ([21, -10], 20, False),
                ([2, -2, -1, -1, 1, 1], 20, False),
                ([100.0, 100.0, 100.0, 100, 100, -100], 100000, False)
            ]
    )
    def test_submit_for_loan(self, create_account, history, amount, expected_info):
        account = create_account()
        account.history = history
        account.balance = sum(history)

        result = account.submit_for_loan(amount)
        assert result == expected_info

        if expected_info:
            assert account.balance == sum(history) + amount
        else:
            assert account.balance == sum(history)