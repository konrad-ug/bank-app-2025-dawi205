from src.account import Account
import requests
from datetime import date
import os

class ProfessionalAccount(Account): 
    MF_url = os.getenv("BANK_APP_MF_URL", "https://wl-api.mf.gov.pl")

    def __init__(self, company_name, NIP):
        super().__init__()
        self.company_name = company_name
        self.balance = 0.0
        if not self.is_NIP_valid(NIP):
            self.NIP="Invalid"
        elif self.is_NIP_real(NIP):
            self.NIP = NIP
        else:
            raise ValueError("Company not registered!!")
        self.express_fee = 5.0

    def is_NIP_valid(self, NIP):
        if len(NIP) == 10 and NIP.isdigit():
            return True
        return False 
    
    def is_ZUS_paid(self, history):
        if -1775 in history:
            return True
        return False
    
    def take_loan(self, amount):
        if (self.is_ZUS_paid(self.history)) and (self.balance >= amount*2):
            self.balance += amount
            return True
        return False
    
    def is_NIP_real(self, NIP):
        today = date.today()
        url = f"{self.MF_url}/api/search/nip/{NIP}?date={today}"
        response = requests.get(url)
        if response.status_code != 200:
            return False
        
        data = response.json() or {}
        result = data.get("result") or {}
        subject = result.get("subject") or {}
        status = subject.get("statusVat") or {}
        print(status)
        return status == "Czynny"


# url = "https://wl-api.mf.gov.pl/api/search/nip/111111111?date=2025-12-13"

# response = requests.get(url)
# today=date.today()
# print(today)
# print(response.status_code)
# data = response.json()

# print(data["result"]["subject"])