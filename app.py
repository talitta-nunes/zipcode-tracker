from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_address', methods=['POST'])
def get_address():
    cep = request.form['cep']
    address_info = get_address_from_cep(cep)
    return jsonify(address_info)

if __name__ == '__main__':
    app.run(debug=True)
