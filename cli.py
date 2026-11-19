import requests

url = 'http://127.0.0.1:5000'


# View all products
def view_inventory():
    response = requests.get(url + '/inventory')
    items = response.json()

    for item in items:
        print("\nID:", item['id'])
        print("Name:", item['product_name'])
        print("Brand:", item['brands'])
        print("Price:", item['price'])
        print("Quantity:", item['quantity'])




#POST a product
def add_product():
    name = input("Product name: ")
    brand = input("Brand: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    data = {
        "product_name": name,
        "brands": brand,
        "price": price,
        "quantity": quantity
    }

    response = requests.post(url + '/inventory', json=data)
    print(response.json())






# Delete a product
def delete_product():
    id = input("Enter product ID: ")

    response = requests.delete(url + '/inventory/' + id)
    print(response.json())












    # Update a product
def update_product():
    id = input("Enter product ID: ")
    price = float(input("New price: "))
    quantity = int(input("New quantity: "))

    data = {
        "price": price,
        "quantity": quantity
    }

    response = requests.patch(url + '/inventory/' + id, json=data)
    print(response.json())



#Menu

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. View inventory")
    print("2. Add product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        view_inventory()
    elif choice == '2':
        add_product()
    elif choice == '3':
        update_product()
    elif choice == '4':
        delete_product()
    elif choice == '5':
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Try again.")
