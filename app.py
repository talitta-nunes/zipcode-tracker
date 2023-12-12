from flask import Flask, render_template, request, jsonify
from utils import get_address_from_cep

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_address', methods=['POST'])
def get_address():
    cep = request.form['cep']
    address_info = get_address_from_cep(cep)
    return jsonify(address_info), cep
# @app.route('/get_coordinate')
# def get_coord():
#     coord = get_address['cep']
#     coord_info = get_coordinate(coord)
#     return jsonify(coord_info)

if __name__ == '__main__':
    app.run(debug=True)
