import pytest
from app.api import app, registry # po AS to nadanie nazwy


@pytest.fixture(autouse=True) # autouse=True, uruchamia się zawsze przed testem i nie trzeba przekazywać jako argument
def clear_registry(): #czyszczenie rejestru kont
    registry.accounts = []
    yield
    registry.accounts = []


@pytest.fixture
def client():
    return app.test_client() # specjalny obiekt do testowania app


@pytest.fixture
def registry_with_accounts(client):
    accounts = [
        {"name": "Jan", "surname": "Kowalski", "pesel": "11111111111"},
        {"name": "Anna", "surname": "Nowak", "pesel": "22222222222"},
        {"name": "Piotr", "surname": "Wiśniewski", "pesel": "33333333333"},
        {"name": "Katarzyna", "surname": "Zielińska", "pesel": "44444444444"}
    ]
    for acc in accounts:
        resp = client.post("/app/accounts", json=acc)
        assert resp.status_code == 201
    return accounts


class Testapp:
    @pytest.mark.parametrize(
        "account_to_add, expected_status_code",
        [
            ({"name": "John", "surname": "Pork", "pesel": "11111111111"}, 201),
            ({"name": "John", "surname": "Pork", "pesel": "12222222222"}, 201),
            ({"name": "John", "surname": "Pork", "pesel": "33333333333"}, 201),
        ]
    )
    def test_create_account(self, client, account_to_add, expected_status_code):
        response = client.post("/app/accounts", json=account_to_add)
        assert response.status_code == expected_status_code

    @pytest.mark.parametrize(
        "pesel_do_wyszukania, expected_status_code",
        [
            ("11111111111", 200),
            ("22222222222", 200),
            ("11111111333", 404),
            ("11122221111", 404),
        ]
    )
    def test_find_by_pesel(self, client, pesel_do_wyszukania, expected_status_code, registry_with_accounts): # test sam uruchamia registry_with_accounts, nawet pomimo niewpisania w kodzie
        response = client.get(f"/app/accounts/{pesel_do_wyszukania}")
        assert response.status_code == expected_status_code

    @pytest.mark.parametrize(
        "pesel, update, expected_status_code",
        [
            ("11111155555", {"name": "Dawid"}, 404),
            ("22222222222", {"name": "Dawid"}, 200),
            ("44444444444", {"surname": "Dawid"}, 200)
        ]
    )
    def test_update_account(self, client, pesel, update, expected_status_code, registry_with_accounts):
        response = client.patch(f"/app/accounts/{pesel}", json=update)
        assert response.status_code == expected_status_code

    @pytest.mark.parametrize(
        "pesel, expected_status_code",
        [
            ("11111111111", 200),
            ("44444444444", 200),
            ("11111114321", 404),
            ("1111111", 404)
        ]
    )
    def test_delete_account(self, client, pesel, expected_status_code, registry_with_accounts):
        response = client.delete(f"/app/accounts/{pesel}")
        assert response.status_code == expected_status_code