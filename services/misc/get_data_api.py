import requests
from ...config import CNPJ_URL, CEP_URL, IBGE_UF_URL

def get_data_from_cnpj(cpf_cnpj):
    url = CNPJ_URL
    endpoint = cpf_cnpj

    response = requests.get(f"{url}/{endpoint}")

    if response.status_code != 200:
        return {
            "error": (f"Requisição à API do CNPJ falhou: {response.json().get('title')}."),
            "status code": (f"Código de status: {response.status_code}.")
        }

    return response.json()


def get_address_from_cep(cep):
    url = CEP_URL
    endpoint = cep

    response = requests.get(f"{url}/{endpoint}")

    if response.status_code != 200:
        return {
            "error": ("Requisição à API do CEP falhou."),
            "status_code": (f"Código de status: {response.status_code}.")
        }

    return response.json()


def get_state_name_from_uf(uf):
    url = IBGE_UF_URL
    endpoint = uf

    response = requests.get(f"{url}/{endpoint}")

    if response.status_code != 200:
        return {
            "error": (f"Requisição à API do IBGE falhou: {response.json().get('message')}"),
            "status_code": (f"Código de status: {response.status_code}.")
        }

    return response.json()

