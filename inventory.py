
from textwrap import dedent
#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoes = []

#========The beginning of the class==========
class Shoe:
    """
    This class defines an class of shoes with attributes country, code, product, cost , and quantity.
    Class method for getting the product name, unit cost, and quantity of class instances are also defined.
    """
    
    def __init__(self, country, code, product, cost, quantity):
        # Initialising class attributes for each instance

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_product(self):
        """Getting the product name of an instance of the class"""

        return self.product
    
    def get_cost(self):
        """Getting the unit cost of an instance of the class"""

        return self.cost
        
    def get_quantity(self):
        """Getting the quantity of an instance of the class"""

        return self.quantity

    def __str__(self):
        """This method prints a string representation of the class instance"""

        return dedent(f"""\
        Product : {self.product}
        Code    : {self.code}
        Cost    : {self.cost}
        Quantity: {self.quantity}
        Country : {self.country}""")

#==========Functions outside the class==============

def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a Shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes.
    '''

    # Opening the inventory txt file
    with open('inventory.txt','r') as shoes_file:
        content = shoes_file.readlines()

        # Using try/except block to get data from the file so we get only the valid data
        for x, line in enumerate(content):
            try:
                shoe_data = line.strip().split(',')
                shoe_cost = int(shoe_data[3])
                shoe_quantity = int(shoe_data[4])

                # Creating and adding objects to the shoes list
                shoes.append(Shoe(shoe_data[0], shoe_data[1], shoe_data[2], int(shoe_data[3]), int(shoe_data[4])))
            except ValueError:
                continue
                

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoes list.
    '''

    while True:
        try:
            # This try block gets shoe attributes from user and checks if the data is in the corret format
            # before creating and adding new objects to the shoes list
            
            shoe_data = input("Please enter shoe data separated by commas in the following order:" \
                "country, code, product name, unit cost, quantity: ")
            shoe_data = shoe_data.strip().split(",") # creates a list from the user's entry

            # Iterating through the list and creating shoe objects
            for x, data in enumerate(shoe_data):
                data = data.strip()
                shoe_data[x] = data
            shoe_cost = int(shoe_data[3])
            shoe_quantity = int(shoe_data[4])
            shoes.append(Shoe(shoe_data[0], shoe_data[1], shoe_data[2], int(shoe_data[3]), int(shoe_data[4])))
            break

        except ValueError: # Handling value errors
            print("Invalid shoe data format or order! Please try again.")
            continue
    
    # Updating inventory file
    update_inventory_file()
    print("\nThe shoe has been successfully added to the inventory!")

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''

    breakout = False # Breaks out of parent loop when true
    while True:

        read_shoes_data() # Getting shoe data from file

        # Printing shoe objects
        for index in range(len(shoes)):
            print(shoes[index], "\n")

        # Navigation to main menu
        while True:
            back = input("Enter 'menu' to go back to the main menu: ")
            if back.strip().lower() == 'menu':
                breakout = True # setting breakout variable for parent loop to True
                break
            else:
                print("Invalid selection! Please try again.\n")
                continue

        if breakout == True:
            break
def get_num(prompt):
    """This function limits user input to integers only where whole numbers are needed"""

    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else:
            print("Invalid entry! Please enter a positive whole number.")
            continue

def update_inventory_file():
    """This function writes shoe objects to text file"""

    # Updating inventory file
    with open('inventory2.txt', 'w+') as file:
        file.write("Country,Code,Product,Cost,Quantity\n")

        for shoe in shoes:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

def re_stock():
    '''
    This function will find the Shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    # Finding product with the lowest quantity
    index_min_quantity = 0
    min_quantity = shoes[index_min_quantity].get_quantity()

    # Finding shoe with lowest quantity
    for x, shoe in enumerate(shoes):
        if shoe.get_quantity() < min_quantity:
            index_min_quantity = x
            min_quantity = shoes[index_min_quantity].get_quantity()

    print("The shoe below has the least stock items:\n")
    print(str(shoes[index_min_quantity])) # Printing shoe with lowest quantity
    
    while True:
        choice = input("Would you like to add stock of this shoe? Y/N: ")
        if choice.strip().lower() == "y":
            additional_quantity = get_num("How much would you like to add? ")
            new_quantity = additional_quantity + shoes[index_min_quantity].get_quantity()
            shoes[index_min_quantity].quantity = new_quantity
            print(f"Quantity for {shoes[index_min_quantity].get_product()} has been updated to {new_quantity}!")
            break
        else:
            break   

    update_inventory_file()

def search_shoe():
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''

    code = input("Enter the code of the shoe: ")
    for shoe in shoes:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    It will then print this information on the console for all the shoes.
    '''

    for shoe in shoes:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} - Value per item: {value}")

def highest_qty():
    '''
    This function determines the product with the highest quantity and
    prints this shoe as being for sale.
    '''

    max_qty = max(shoe.get_quantity() for shoe in shoes)
    for shoe in shoes:
        if shoe.get_quantity() == max_qty:
            print(f"This shoe is on sale: {shoe.get_product()}")

#==========Main Menu=============
def main():
    while True:
        """This while loop will keep the program running until the user intentionally exits."""

        # Menu navigation
        choice = input(dedent("""\
        WELCOME TO THE SHOE INVENTORY MANAGEMENT
        
        Please choose an option to get started:

        1. Add a shoe
        2. View all shoes
        3. Search for a shoe
        4. Check stock monetary values
        5. Find and put on sale the shoe with the highest stock quantity
        6. Re-stock the shoe with the lowest stock quantity
        7. Quit
        
        Enter your choice (you can enter 7 or 'exit' to leave the program): """)

        )
        if choice == '1':
            capture_shoes()
        elif choice == '2':
            view_all()
        elif choice == '3':
            search_shoe()
        elif choice == '4':
            value_per_item()
        elif choice == '5':
            highest_qty()
        elif choice == '6':
            re_stock()
        elif choice == '7':
            break
        elif choice == 'exit':
            exit()
        else:
            print("Invalid choice. Please try again.")

# Starting the program
main()