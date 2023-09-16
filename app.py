from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('data.json', 'r') as file:
    products = json.load(file)

@app.route('/')
def home():
    return('<div style="display: flex; flex-direction: column; justify-content: center; align-items: center"><h1 style="text-align:center;">Backend UMKM</h1><p>ini adalah contoh backend sederhana dengan python Flask</p></div>')
@app.route('/api/products', methods=['GET'])
def get_all_products():
    sorted_products = sorted(products, key=lambda x: x['nama'])  # Mengurutkan produk berdasarkan nama
    response = {
        "status": "Success",
        "message": "API produk berhasil diakses.",
        "products": sorted_products
    }
    return jsonify(response)

@app.route('/api/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '').lower()  # Mengambil parameter pencarian dari URL

    # Mencari produk yang sesuai dengan query
    matching_products = [product for product in products if query in product['nama'].lower()]

    sorted_matching_products = sorted(matching_products, key=lambda x: x['nama'])  # Mengurutkan hasil pencarian

    response = {
        "status": "Success",
        "message": "Hasil pencarian produk",
        "products": sorted_matching_products
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
