from flask import Flask, render_template, request, jsonify
from utils import get_address_from_cep
import geopandas as gpd
from geopy.geocoders import Nominatim

app = Flask(__name__)

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
