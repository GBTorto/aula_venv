import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("API_KEY")

print(api_key)

requisicao = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD")
dados = requisicao.json()

conversao_moedas = dados["conversion_rates"]

for moedas, valor in conversao_moedas.items():
    print(f"{moedas}: {valor}")