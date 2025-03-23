from config import CPF_LEN

SERVICOS = ["CQ Intra", "LR Intra", "EPI"]


def clean_null(data):
    clean_data = {
        key: value for key, value in data.items() if value and str(value).strip()
    }
    return clean_data


def selecionar_servicos():
    servicos_selecionados = []

    print("\nSelecione os serviços:")
    for servicos in enumerate(SERVICOS, start=1):
        print(servicos)

    selecao = input("\nDigite o numero dos servicos desejados, separados por vírgula: ")
    try:
        indices = [int(x.strip()) - 1 for x in selecao.split(",")]

        for index in indices:
            if index < 0 or index >= len(SERVICOS):
                print(f"Seleção inválida: {index+1}. Tente novamente.")

            servico_selecionado = SERVICOS[index]
            servicos_selecionados.append({index: servico_selecionado})

            print(f"servico {servico_selecionado} adicionado.")

    except ValueError:
        print("Input inválida.")

    return servicos_selecionados


def main_form(razao_social=None, cep=None, numero_endereco=None):

    cpf_cnpj = input("CPF/CNPJ: ")
    if len(cpf_cnpj) <= CPF_LEN:
        razao_social = input("Nome Completo: ")
        cep = input("CEP: ")
        numero_endereco = input("Nº do endereço: ")
    email_cliente = input("Email: ")
    fone_cliente = input("Telefone: ")
    servicos_selecionados = selecionar_servicos()

    dados_orcamento = {
        "cpf_cnpj": cpf_cnpj,
        "razao_social": razao_social,
        "cep": cep,
        "numero_endereco": numero_endereco,
        "email_cliente": email_cliente,
        "fone_cliente": fone_cliente,
        "servicos_selecionados": servicos_selecionados,
    }

    return clean_null(dados_orcamento)
