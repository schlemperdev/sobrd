# import forms.main_form as form
from services.omie.get_requests import get_omie_clientes

def main():
    # dados_orcamento = form.main_form()
    # print(dados_orcamento)

    omie = get_omie_clientes(37319901000151)
    print(omie)

if __name__ == "__main__":
    main()
