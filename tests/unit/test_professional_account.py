import pytest
import requests
from src.account import Account
from src.professional_account import ProfessionalAccount

@pytest.fixture
def create_account():
    def create(company_name="Company", NIP="1"):
        return ProfessionalAccount(company_name, NIP)
    return create

@pytest.fixture
def account_with_2k(create_account):
    account = create_account(NIP="1")
    account.balance = 2000
    return account

@pytest.fixture
def mock_mf_api(mocker):
    fake_json = {
        "result": {
            "subject": {
                "statusVat": "Czynny",
                "name": "COMPANY",
                "nip": "0000000000"
            }
        }
    }
    
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = fake_json
    
    patcher = mocker.patch("requests.get", return_value=mock_response)
    
    return patcher

@pytest.fixture
def mock_mf_api_400(mocker):
    fake_json = {
        "code": "WL-115",
        "message": "Nieprawidłowy NIP."
    }
    
    mock_response = mocker.Mock()
    mock_response.status_code = 400
    mock_response.json.return_value = fake_json
    
    patcher = mocker.patch("requests.get", return_value=mock_response)
    
    return patcher

class TestProfessioinalAccount:

    @pytest.mark.parametrize(
            "NIP, expected_info",
            [
                ("8471106989", "8471106989"),
                ("123456789000000", "Invalid"),
                ("123456abcd", "Invalid"),
                ("123", "Invalid"),
            ]
    )
    def test_NIP(self, create_account, NIP, expected_info, mock_mf_api):
        account = create_account(NIP=NIP)
        assert account.NIP == expected_info

    def test_NIP_exception(self, create_account, mock_mf_api):
        mock_mf_api.return_value.json.return_value["result"]["subject"]["statusVat"] = "Zwolniony"
        with pytest.raises(ValueError, match="Company not registered!!"):
            create_account(NIP="8471106989")

    def test_NIP_400(self, create_account, mock_mf_api_400):
        with pytest.raises(ValueError, match="Company not registered!!"):
            create_account(NIP="8471106989")
        
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