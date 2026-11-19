
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Mock database
inventory = [
    {
        "id": 1,
        "product_name": "Milk",
        "brands": "Brookside",
        "price": 100,
        "quantity": 20
    },
    {
        "id": 2,
        "product_name": "Bread",
        "brands": "Supaloaf",
        "price": 60,
        "quantity": 15
    }
]

url = 'https://world.openfoodfacts.net/api/v3.6/product/3274080005003.json'


@app.route('/')
def index():
    return "The landing page"


# GET all items
@app.route('/inventory', methods=['GET'])
def get_items():

    return jsonify(inventory), 200


# GET a specific item
@app.route('/inventory/<int:id>', methods=['GET'])
def get_item(id):

    for item in inventory:
        if item['id'] == id:
            return jsonify(item), 200

    return jsonify({"message": "Item not found"}), 404


# POST a new item
@app.route('/inventory', methods=['POST'])
def post_item():

    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "product_name": data['product_name'],
        "brands": data['brands'],
        "price": data['price'],
        "quantity": data['quantity']
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


# PATCH an item
@app.route('/inventory/<int:id>', methods=['PATCH'])
def update_item(id):

    data = request.get_json()

    for item in inventory:
        if item['id'] == id:

            item['price'] = data.get('price', item['price'])
            item['quantity'] = data.get('quantity', item['quantity'])

            return jsonify(item), 200

    return jsonify({"message": "Item not found"}), 404


# DELETE an item
@app.route('/inventory/<int:id>', methods=['DELETE'])
def remove_item(id):

    for item in inventory:
        if item['id'] == id:

            inventory.remove(item)

            return jsonify({"message": "Item deleted"}), 200

    return jsonify({"message": "Item not found"}), 404


# GET product from OpenFoodFacts
@app.route('/lookup', methods=['GET'])
def lookup_product():

    response = requests.get(url)

    info = response.json()

    return jsonify(info), 200


if __name__ == "__main__":
    app.run(debug=True)
