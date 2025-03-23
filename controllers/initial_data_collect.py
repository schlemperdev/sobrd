import services.misc.get_data_api as get_misc
from config import CNPJ_LEN, CPF_LEN, DADOS_TESTE  # teste
from utils.data_manipulation import salvar_json


def collect_data_with_form_input(dados_form=DADOS_TESTE):
    cpf_cnpj = dados_form.get("CPF")  # teste

    full_data = []
    filename = "repos/json/full_data.json"

    # Handle for CNPJ input
    if len(cpf_cnpj) == CNPJ_LEN:
        cnpj_api_data = get_misc.get_data_from_cnpj(cpf_cnpj)
        if "error" in cnpj_api_data and cnpj_api_data["error"]:
            print(cnpj_api_data)
            return
        full_data.append({"cnpj_api_data": cnpj_api_data})
        cep = cnpj_api_data.get("cep")

    # Handle for CPF input
    if len(cpf_cnpj) == CPF_LEN:
        full_data.append({"dados_orcamento": dados_form})
        cep = dados_form.get("CEP")

    # Get address from cep
    address_from_cep = get_misc.get_address_from_cep(cep)
    if "error" in address_from_cep and address_from_cep["error"]:
        print(address_from_cep)
        return
    full_data.append({"address_from_cep": address_from_cep})
    uf = address_from_cep.get("state")

    # Get state name from uf
    state_name = get_misc.get_state_name_from_uf(uf)
    if "error" in state_name and state_name["error"]:
        print(state_name)
        return
    full_data.append({"state_name": state_name})

    # Save data and end return
    salvar_json(full_data, filename)
    return full_data
