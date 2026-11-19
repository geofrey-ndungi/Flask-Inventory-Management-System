# Flask Inventory Management System

A small Flask REST API with in-memory inventory storage, an OpenFoodFacts product
lookup, and a command-line client.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API listens at `http://127.0.0.1:5000`. Inventory is kept in memory and is
reset to the sample item each time the server restarts.

## REST API

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/inventory` | List inventory items |
| `GET` | `/inventory/<id>` | Get one item |
| `POST` | `/inventory` | Add an item |
| `PATCH` | `/inventory/<id>` | Update supplied item fields |
| `DELETE` | `/inventory/<id>` | Delete an item |
| `GET` | `/products/search?barcode=<code>` | Look up a product by barcode |
| `GET` | `/products/search?name=<text>` | Search products by name |

Inventory creation requires `name`, `price`, and `quantity`. For example:

```bash
curl -X POST http://127.0.0.1:5000/inventory \
  -H 'Content-Type: application/json' \
  -d '{"name":"Almond milk","price":4.99,"quantity":24,"barcode":"3274080005003"}'
```

Prices and quantities must be non-negative; quantity must be an integer. Product
search results include the name, brand, barcode, ingredients, image URL, and
categories returned by OpenFoodFacts. A failed upstream request returns HTTP 502.

## CLI

Run commands from the project directory while the API is running. The optional
`--api-url` argument changes the API base URL.

```bash
python cli.py list
python cli.py get 1
python cli.py add --name "Almond milk" --price 4.99 --quantity 24 \
  --brand Silk --barcode 3274080005003
python cli.py update 1 --price 5.25 --quantity 12
python cli.py delete 1
python cli.py search --barcode 3274080005003
python cli.py search --name "almond milk"
```

## Tests

```bash
python -m unittest discover -s tests
```
