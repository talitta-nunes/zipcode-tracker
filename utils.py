import requests

def get_address_from_cep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        response.raise_for_status()  

        data = response.json()
        if not data.get("erro"):
            address = {
                "cep": data["cep"],
                "logradouro": data["logradouro"],
                "complemento": data.get("complemento", ""),
                "bairro": data["bairro"],
                "localidade": data["localidade"],
                "uf": data["uf"]
            }
            return address
        else:
            print("Address not found for the provided CEP.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from ViaCEP api: {e}")
        return None
    except ValueError as e:
        print(f"An error occurred while parsing the JSON response: {e}")
        return None






