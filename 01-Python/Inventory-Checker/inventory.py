
#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"Country: {self.country} | Code: {self.code} | "
                f"Product: {self.product} | Cost: {self.cost} | "
                f"Quantity: {self.quantity}")


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============

def read_shoes_data():
    try:
        with open("Code Files/inventory.txt", "r") as file:
            next(file)  # skip header line

            for line in file:
                data = line.strip().split(",")

                if len(data) == 5:
                    country, code, product, cost, quantity = data
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)

        print("Data loaded successfully.\n")

    except FileNotFoundError:
        print("Error: inventory.txt file not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
  
def capture_shoes():
    print("\nEnter new shoe details:")

    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = float(input("Cost: "))
    quantity = int(input("Quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    # Save to file
    with open("inventory.txt", "a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")

    print("Shoe added successfully.\n")

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():

    print("\n--- Shoe Inventory ---")
    for shoe in shoe_list:
        print(shoe)
    print()

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    if not shoe_list:
        print("No data available.")
        return

    lowest_shoe = min(shoe_list, key=lambda x: x.quantity)

    print("\nLowest stock item:")
    print(lowest_shoe)

    choice = input("Do you want to restock this item? (yes/no): ").lower()

    if choice == "yes":
        add_qty = int(input("Enter quantity to add: "))
        lowest_shoe.quantity += add_qty

        # Rewrite file
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

        print("Stock updated successfully.\n")

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe():
    code = input("Enter shoe code to search: ")

    for shoe in shoe_list:
        if shoe.code == code:
            print("\nShoe found:")
            print(shoe)
            return

    print("Shoe not found.\n")

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    print("\n--- Value Per Item ---")

    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} (Code: {shoe.code}) - Value: {value}")

    print()

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    if not shoe_list:
        print("No data available.")
        return

    highest = max(shoe_list, key=lambda x: x.quantity)

    print
    ("\n--- Item For Sale (Highest Quantity) ---")
    print(highest)
    print()
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

def menu():
    read_shoes_data()

    while True:
        print("===== Shoe Inventory Menu =====")
        print("1. View all shoes")
        print("2. Add new shoe")
        print("3. Restock shoes")
        print("4. Search shoe")
        print("5. Value per item")
        print("6. Highest quantity item")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


# Run program
menu()