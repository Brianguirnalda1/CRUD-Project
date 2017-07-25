import csv

products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for ordered_dict in reader:
        products.append(dict(ordered_dict))#from class thank you Prof Rossetti

menu = """

------------------------------------
BRIAN'S AWESOME PRODUCTS APPLICATION
------------------------------------
Hello and welcome {0},

There are {1} products in the database. Please select an operation:

    operation | description
    --------- | ------------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new prodcut.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.


""".format("Brianguirnalda1", len(products))

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

def list_products():
    print("THERE ARE", len(products), "PRODUCTS:")
    for product in products:
        print("  +", product)
    return (products)

def show_product():
    product_id = input("OK. Please specify the product's identifer: ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("Showing the product here!", product)
    else:
        print("Could not find the product identifer", product)

def create_product():
    print("CREATING A PRODUCT")
    product_name = input("name is:")
    product_aisle = input("aisle is:")
    product_department = input("department is:")
    product_price = input("price is:")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
}
    print("NEW PRODUCT IS", new_product)
    products.append(new_product)

headers = ["id", "name", "aisle", "department", "price"]
user_input_headers = [header for header in headers if header != "id"]

def update_product():
    product_id = input("OK. Please specify the product's identifer: ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("OK. Please specify the products information:")
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("UPDATING PRODUCT HERE!", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

def destroy_product():
    product_id = input("OK. Please specify the product's identifier: ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT HERE", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)
