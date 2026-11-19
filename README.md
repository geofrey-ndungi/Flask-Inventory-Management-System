# Inventory Management System

## 1. Project Overview

The Inventory Management System is a simple Python application built
with Flask. It provides a REST API for managing inventory items and a
command-line interface (CLI) that allows a user to interact with the
API.

The application uses a Python list as a temporary mock database.
Inventory data is stored in memory while the Flask application is
running. The data is reset when the server is stopped.

## 2. Project Objectives

The project is designed to:

-   Display all inventory items.
-   Retrieve a single inventory item using its ID.
-   Add new inventory items.
-   Update existing inventory items.
-   Delete inventory items.
-   Provide a command-line interface for using the inventory API.
-   Integrate with the Open Food Facts API to retrieve product
    information, as required by the project specification.

## 3. Technologies Used

  Technology            Purpose
  --------------------- -------------------------------------------------------
  Python                Main programming language
  Flask                 Creates the REST API
  Requests              Sends HTTP requests from the CLI and to external APIs
  Postman               Tests the REST API endpoints
  Open Food Facts API   Provides external product information

## 4. Project Structure

A simple project structure is:

``` text
inventory-management-system/
├── app.py
├── cli.py
└── README.md
```

-   `app.py` contains the Flask application, inventory data and API
    endpoints.
-   `cli.py` contains the command-line interface used to interact with
    the Flask API.
-   `README.md` contains the project documentation.

## 5. Inventory Data

The application uses a Python list as a mock database. Each inventory
item contains the following fields:

  Field            Description
  ---------------- --------------------------------
  `id`             Unique identifier for the item
  `product_name`   Name of the product
  `brands`         Product brand
  `price`          Price of the product
  `quantity`       Number of units available

Example inventory item:

``` json
{
    "id": 1,
    "product_name": "Milk",
    "brands": "Brookside",
    "price": 100,
    "quantity": 20
}
```

Because the application uses an in-memory list, changes are not
permanently saved. The original sample data is loaded again when the
Flask server restarts.

## 6. REST API Endpoints

The Flask application provides the following endpoints:

  HTTP Method   Endpoint            Description
  ------------- ------------------- ---------------------------------
  GET           `/inventory`        Retrieves all inventory items
  GET           `/inventory/<id>`   Retrieves one item using its ID
  POST          `/inventory`        Adds a new inventory item
  PATCH         `/inventory/<id>`   Updates an existing item
  DELETE        `/inventory/<id>`   Deletes an item

### 6.1 Retrieve All Inventory Items

**Request**

``` http
GET http://127.0.0.1:5000/inventory
```

Returns a list of all items in the inventory.

### 6.2 Retrieve One Inventory Item

**Request**

``` http
GET http://127.0.0.1:5000/inventory/1
```

Returns the item with ID `1`.

If the item does not exist, the API returns a `404 Not Found` response.

### 6.3 Add an Inventory Item

**Request**

``` http
POST http://127.0.0.1:5000/inventory
```

**Example JSON body**

``` json
{
    "product_name": "Mala",
    "brands": "Brookside",
    "price": 80,
    "quantity": 25
}
```

The API adds the new item and returns the created item with a
`201 Created` status code.

### 6.4 Update an Inventory Item

**Request**

``` http
PATCH http://127.0.0.1:5000/inventory/1
```

**Example JSON body**

``` json
{
    "price": 120
}
```

The API updates the supplied fields for the item with ID `1`. Fields not
included in the request remain unchanged.

### 6.5 Delete an Inventory Item

**Request**

``` http
DELETE http://127.0.0.1:5000/inventory/1
```

The API deletes the item with ID `1`. If the item does not exist, it
returns a `404 Not Found` response.

## 7. Command-Line Interface

The CLI is implemented in `cli.py`. It sends HTTP requests to the Flask
API using the Requests library.

The menu provides these options:

1.  View inventory
2.  Add product
3.  Update product
4.  Delete product
5.  Exit

The CLI requires the Flask server to be running before it can
communicate with the API.

## 8. Open Food Facts API Integration

The project specification includes integration with the Open Food Facts
API to retrieve product information using a barcode or product name.

Official API documentation:

https://openfoodfacts.github.io/openfoodfacts-server/api/

The external API integration should be implemented and tested in the
Flask application. The CLI menu documented above contains the four
inventory management operations and does not include a separate product
lookup option.

## 9. Running the Application

### Step 1: Install the required packages

Open a terminal in the project directory and run:

``` bash
pip install flask requests
```

### Step 2: Start the Flask server

Run:

``` bash
python app.py
```

The Flask development server will normally be available at:

``` text
http://127.0.0.1:5000
```

Keep this terminal open while using the CLI.

### Step 3: Start the CLI

Open a second terminal in the project directory and run:

``` bash
python cli.py
```

Follow the menu instructions to manage inventory items.

## 10. Testing

Postman can be used to test the REST API endpoints.

The following tests should be performed:

  Test                              Expected result
  --------------------------------- -----------------------------------------
  Retrieve all items                Returns the inventory list
  Retrieve an existing ID           Returns the matching item
  Retrieve a missing ID             Returns `404 Not Found`
  Add an item                       Returns the new item with `201 Created`
  Update an existing item           Returns the updated item
  Delete an existing item           Returns a confirmation message
  Delete or retrieve a missing ID   Returns `404 Not Found`

The CLI should also be tested by selecting each menu option and checking
that the expected operation is performed.

## 11. Limitations

-   The inventory is stored in a Python list rather than a permanent
    database.
-   Inventory changes are lost when the Flask server stops.
-   The application is intended for learning and demonstration purposes.
-   The Flask development server is not intended for production
    deployment.

## 12. Conclusion

The Inventory Management System demonstrates how to build a basic REST
API using Flask and how to interact with that API through a command-line
interface. It covers the main CRUD operations: Create, Read, Update and
Delete. The project also includes an external API integration
requirement using Open Food Facts.
