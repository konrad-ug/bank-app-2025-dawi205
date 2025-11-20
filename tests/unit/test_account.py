import pytest
from src.account import Account

@pytest.fixture
def create_account():
    return Account

@pytest.fixture
def account_with_500(create_account):
    account = create_account()
    account.balance = 500
    account.express_fee = 5
    return account

class TestAccount:

    @pytest.mark.parametrize(
            "amount, expected_history, expected_balance, expected_info1, expected_info2",
            [
                (50, [-50, 100, -50], 500, True, True),
                (1000, [2000, -1000], 1500, False, True),
                (500, [-500, 1000, -500], 500, True, True),
                (550, [1100, -550], 1050, False, True),
            ]
    )
    def test_history(self,account_with_500, amount, expected_history, expected_info1, expected_info2, expected_balance):
        account = account_with_500
        info1 = account.outcoming_transfer(amount)
        account.incoming_transfer(amount*2)
        info2 = account.outcoming_transfer(amount)
        assert info1 == expected_info1
        assert account.history == expected_history
        assert info2 == expected_info2
        assert account.balance == expected_balance
        
    @pytest.mark.parametrize(
                "amount, expected_history, expected_balance, expected_info1, expected_info2",
                [
                    (50, [-50, -5, 100, -50, -5], 490, True, True),
                    (1000, [2000, -1000, -5], 1495, False, True),
                    (500, [-500, -5, 1000, -500, -5], 490, True, True),
                    (550, [1100, -550, -5], 1045, False, True),
                ]
    )
    def test_history_with_express_transfers(self, account_with_500, amount, expected_history, expected_balance, expected_info1, expected_info2):
        account = account_with_500
        info1 = account.outcoming_express_transfer(amount)
        account.incoming_transfer(amount*2)
        info2 = account.outcoming_express_transfer(amount)
        assert info1 == expected_info1
        assert account.history == expected_history
        assert info2 == expected_info2
        assert account.balance == expected_balance        