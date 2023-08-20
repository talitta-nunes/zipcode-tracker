import requests

def get_address_from_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if not data.get("erro"):
            return {
                "cep": data["cep"],
                "logradouro": data["logradouro"],
                "complemento": data.get("complemento", ""),
                "bairro": data["bairro"],
                "localidade": data["localidade"],
                "uf": data["uf"]
            }
        else:
            return None
    else:
        return None


