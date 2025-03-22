import requests
from config import HEADERS, OMIE_URL, OMIE_APP_KEY, OMIE_APP_SECRET

def get_omie_clientes(cpf_cnpj):
    endpoint = "geral/clientes/"
    url = OMIE_URL + endpoint

    clientesFiltro = {"clientesFiltro": {"cnpj_cpf": cpf_cnpj}}
    payload = {
        "call": "ListarClientes",
        "app_key": (f"{OMIE_APP_KEY}"),
        "app_secret": (f"{OMIE_APP_SECRET}"),
        "param": [clientesFiltro]
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code != 200:
        return {
            "error": (f"Erro ao Listar Clientes na API do OMIE: {response.json().get('faultstring')}"),
            "status_code": (f"Código de status: {response.status_code}")
        }

    return response.json()
