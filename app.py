
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__) #recomendação do flask. sempre.

#sempre tem um route e uma função. Routo o caminho que o site terá, homepage.
# função, o que eu desejo exibir nessa página.
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

# Example usage
cep = input("Enter the CEP: ")
address_info = get_address_from_cep(cep)

if address_info:
    print("Address:")
    print(f"CEP: {address_info['cep']}")
    print(f"Logradouro: {address_info['logradouro']}")
    print(f"Complemento: {address_info['complemento']}")
    print(f"Bairro: {address_info['bairro']}")
    print(f"Localidade: {address_info['localidade']}")
    print(f"UF: {address_info['uf']}")
else:
    print("Address not found for the provided CEP.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_address', methods=['POST'])
def get_address():
    cep = request.form['cep']
    address_info = get_address_from_cep(cep)
    return jsonify(address_info)
##irei exexutar esse codigo se esse arquivo for executado, colocando o site no ar

if __name__ == '__main__':
    app.run(debug=True)

