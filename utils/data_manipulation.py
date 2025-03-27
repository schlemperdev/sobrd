import json


def salvar_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return file


def clean_null(data):
    clean_data = {
        key: value for key, value in data.items() if value and str(value).strip()
    }
    return clean_data


def formatar_dados():

    return
