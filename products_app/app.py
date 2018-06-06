import csv
import os

def menu(username, products_count):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
        'Reset'   | Reset list to original state.
     """ # end of multi- line string. also using string interpolation
    return menu


def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            #print(row["name"], row["price"])
            products.append(dict(row))
    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")

    with open(filepath, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
        writer.writeheader()
        for p in products:
            writer.writerow(p)

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)

def run():
    # First, read products from file...
    products = read_products_from_file() # reading products from file and passing it into a variable called products

    # Then, prompt the user to select an operation...
    print(menu(username="Inventory Manager", products_count=len(products))) #TODO instead of printing, capture user input
    choice =(input("Please select an operation:")).lower()
    print(choice)
    if choice == "list":
        print("* * * * * * * * * * * * * * *")
        print(f"LISTING {len(products)} PRODUCTS")
        print("* * * * * * * * * * * * * * *")
        for p in products:
            print("#" +p["id"] +": " + p["name"])

    elif choice == "show":
        accepted_ids = [(p["id"]) for p in products] # list of accepted IDs: 1-20
        showproduct=[] #new list to add selected product
        productid=(input("Ok. Please provide Product ID:")) #ask for product ID
        while productid not in accepted_ids:
            productid = input("Product ID Not Found. Please provide valid product ID:")
        showproduct = [product for product in products if product["id"] == productid]
        print(showproduct)

    elif choice == "create":
        accepted_ids = [int((p["id"])) for p in products]
        newproductid = max(accepted_ids)+1
        newname=(input("Ok. Please provide the name of the new product:"))
        newaisle=(input("Ok. Please provide the aisle of the new product:"))
        newdepartment=(input("Ok. Please provide the department of the new product:"))
        while True:
            try:
                newprice=(input("Ok. Please provide the price of the new product:"))
                while newprice != '{0:.2f}'.format(float(newprice)):
                    newprice=((input("PRICE NOT IN 'x.xx' FORMAT. PLEASE PROVIDE PRICE IN 'x.xx' FORMAT:")))
                products.append({"id": str(newproductid),"name": newname,"aisle": newaisle, "department": newdepartment, "price":newprice})
                showproduct = [product for product in products if product["id"] == str(newproductid)]
                print("* * * * * * * * * * * * * * *")
                print("CREATING NEW PRODUCT")
                print("* * * * * * * * * * * * * * *")
                print(showproduct)
                break
            except ValueError:
                print("PRICE NOT IN 'x.xx' FORMAT. PLEASE PROVIDE PRICE IN 'x.xx' FORMAT:")

    elif choice == "update":
        accepted_ids = [(p["id"]) for p in products] # list of accepted IDs: 1-20
        updateid=(input("Ok. Please provide the ID of the product you want to update:"))
        while updateid not in accepted_ids:
            updateid = input("Product ID Not Found. Please provide valid product ID:")
        updatename=(input("Ok. What is the product's new name?"))
        updateaisle=(input("Ok. What is the product's new aisle?"))
        updatedepartment=(input("Ok. What is the product's new department?"))
        while True:
            try:
                updateprice=(input("Ok. What is the product's new price?"))
                while updateprice != '{0:.2f}'.format(float(updateprice)):
                    updateprice=((input("PRICE NOT IN 'x.xx' FORMAT. PLEASE PROVIDE PRICE IN 'x.xx' FORMAT:")))
                mutateproduct = [product for product in products if product["id"] == updateid][0]
                mutateproduct["name"]= updatename
                mutateproduct["aisle"]= updateaisle
                mutateproduct["department"]= updatedepartment
                mutateproduct["price"]= updateprice
                print("ITEM #" + str(mutateproduct["id"]) + " NOW UPDATED IN INVENTORY!")
                print(mutateproduct)
                break
            except ValueError:
                print("PRICE NOT IN 'x.xx' FORMAT. PLEASE PROVIDE PRICE IN 'x.xx' FORMAT:")

    elif choice == "destroy":
        accepted_ids = [(p["id"]) for p in products]
        destroyid=input("What is the ID of the product that you want to destroy?")
        while destroyid not in accepted_ids:
            destroyid = input("Product ID Not Found. Please provide valid product ID:")
        destroyproduct = [product for product in products if product["id"] == destroyid][0]
        print("DELETED PRODUCT #" + str(destroyproduct["id"]) + " FROM INVENTORY!")
        del products[products.index(destroyproduct)]



    elif choice == "reset":
        reset_products_file()
        return
    else:
        print("Sorry, the operation you selected is not recognized. Please select one of the following: 'List, 'Show', 'Create', 'Update', 'Destroy', or 'Reset'")

    write_products_to_file(products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
