from flask import Flask, request, jsonify
from src.personal_acocunt import PersonalAccount
from src.personal_acocunt import AccountRegistry


app = Flask(__name__)
registry = AccountRegistry()

@app.route("/app/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    account = PersonalAccount(data["name"], data["surname"], data["pesel"])

    if registry.find_by_pesel(account.pesel) is not None:
        return jsonify({"messege": "Account with this PESEL already exists."}), 409

    registry.add_account(account)
    return jsonify({"message": "Account created"}), 201


@app.route("/app/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.get_all_accounts()
    accounts_data = [
        {"name": acc.first_name, "surname": acc.last_name, "pesel": acc.pesel, "balance": acc.balance}
        for acc in accounts
    ]
    return jsonify(accounts_data), 200

@app.route("/app/accounts/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    count = registry.number_of_accounts()
    return jsonify({"count": count}), 200

@app.route("/app/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    account = registry.find_by_pesel(pesel)
    if account:
        account_data = {
            "name": account.first_name,
            "surname": account.last_name,
            "pesel": account.pesel,
            "balance": account.balance
        }
        return jsonify(account_data), 200
    else:
        return jsonify({"message": "Account not found"}), 404

@app.route("/app/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    data = request.get_json()
    account = registry.find_by_pesel(pesel)

    if account:
        if "name" in data:
            account.first_name = data["name"]
        if "surname" in data:
            account.last_name = data["surname"]
        return jsonify({"message": "Account updated"}), 200
    else:
        return jsonify({"message": "Account not found"}), 404

@app.route("/app/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    result = registry.remove_account(pesel)
    if result:
        return jsonify({"message": "Account deleted"}), 200
    else:
        return jsonify({"message": "Account not found"}), 404