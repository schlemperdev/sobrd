import requests
from config import SPOTTER_HEADERS, SPOTTER_URL, TOKEN_EXACT

def get_spotter_organizations(cpf_cnpj):
    endpoint = "/organization"
    filter = (f"?filter=cpfCnpj eq '{cpf_cnpj}'")
    url = SPOTTER_URL + endpoint + filter

    response = requests.get(url, headers=SPOTTER_HEADERS)

    if response.status_code != 200:
        return {
            "error": (f"Erro ao listar organizações na API do Spotter: {response.json().get('message')}"),
            "status_code": (f"Código de status: {response.status_code}")
        }

    return response.json()
