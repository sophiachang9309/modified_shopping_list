#Name: Sophia Chang
#Class: AM

from datetime import datetime

#dictionary called products, which has prodcuts and their prices
products = {
    "Cookies" : 4.0,
    "Custard" : 2.0,
    "Cupcake" : 5.0,
    "Macaron" : 3.0,
    "Strudel" : 4.0
}

#dictionary called shopping_list, which has products and the quantity of each
shopping_cart = {
}

#Option 1
def display_products(prod):
    print("========== AVAILABLE PRODUCTS ==========")
    #iterates through the dictionary to be able to print every single key and value 
    for i, (product,price) in enumerate(prod.items(),1):
        print(f"{i}. {product} : ${price:.2f}")

#Option 2
def add_product(shopping_cart, products):
    print("Products")
    #iterates through the dictionary to be able to print every single key 
    for i, (product) in enumerate(products.keys(),1):
        print(f"{i}. {product}")

    #allows the user to choose which product they'd like to add to their shopping_cart
    product = int(input("Choose an available product from the list.: "))

    #verifies that the item number chosen is valid
    while product < 0 or product > len(products):
        #invalidates the product chosen
        print("That's not a valid product")
        #allows the user to choose which product they'd like to add to their shopping_cart
        product = int(input("Choose an available product from the list.: "))

    #allows the user to choose how much of a product that they'd like to buy
    unit = int(input(f"How much {list(products)[product-1]} would you like to add?:"))

    #verifies that the quantity of the product is valid
    while unit <= 0:
        #invalidates the number chosen
        print("That's not a valid number")
        #allows the user to choose how much of a product that they'd like to buy
        unit = int(input(f"How much {list(products)[product-1]} would you like to add?:"))
    #tells the user what and how much was added to the shopping cart
    print(f"Added {unit} {list(products)[product-1]} to your shopping cart!")
    #checks whether or not the product was already added to the shopping cart
    if product not in shopping_cart:
        shopping_cart[list(products)[product-1]] = unit
        print(f"{list(products)[product-1]} quantity is now {shopping_cart[list(products)[product-1]]}.")

    #if the product was added already, you add the amount that the user
    else:
        unit += shopping_cart[list(products)[product-1]]
    #prints the product and how much of that product is in the shopping_cart
    print(f"{list(products)[product-1]} quantity is now {shopping_cart[list(products)[product-1]]}.")

#Option 3
def remove_product(shopping_cart):
    print("Shopping cart")
    #iterates through the dictionary to be able to print every single key 
    for i, (product,quantity) in enumerate(shopping_cart.items(),1):
        print(f"{i}. {product} - Quantity: {quantity}")
    #this functions when there is actually something in the shopping_cart
    if len(shopping_cart) != 0:
        remove = int(input("What item would you like to delete?(choose a number)"))
        #checks if the user's number to remove is in the right range
        while remove < 1 or remove > len(shopping_cart):
            print("Invalid number")
            remove = int(input("What item would you like to delete?(choose a number)"))
        #the list(shopping_cart)[remove - 1] part gets you the key, but the overall function of this is to get subtract one from the quantity
        new = shopping_cart[list(shopping_cart)[remove - 1]] - 1

        #this removes the key form the shopping cart
        print(f"Removed 1 {list(shopping_cart)[remove-1]} from your cart!")

        #this sets the key to the new value 
        shopping_cart[list(shopping_cart)[remove - 1]] = new

        #checks whether or not the quantity reached 0, completely removes it from the cart
        if shopping_cart[list(shopping_cart)[remove - 1]] <= 0:
            #list(shopping_cart)[remove - 1] is the product/key and this print statement prints that it's been removed
            print(f"{list(shopping_cart)[remove - 1]} has been completely removed from your cart.")
            #This gets rid of a product
            del shopping_cart[list(shopping_cart)[remove - 1]]
        #this starts when the quantity isn't 0 or less
        else:
            print(f"{list(shopping_cart)[remove - 1]} quantity is now {shopping_cart[list(shopping_cart)[remove - 1]]} ")
    #this functions when there is nothing in the shopping cart
    else:
        print("There's nothing in your shopping cart to remove.")

#Option 4
def display_cart(shopping_cart,products):
    print("========== YOUR SHOPPING CART ==========")

    #checks whether the shopping_cart list is empty. in other words, it checks if the cart is empty
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty.")

    #functions when the shopping_cart list isn't empty. in other words, it works when the cart is not empty
    else:
        #quantity variable
        q = 0
        #displays everything currently in the shopping cart
        for i, (product,value) in enumerate(shopping_cart.items(),1):
            #sees whether or not the key from shopping_list is in the products' dictionary
            if product in products:
                #gets the unit price from the products dictionary
                unit_price = products[list(shopping_cart)[i-1]]
                print("Product:")
                print(f"{i}. {product}")
                print("Unit Price:")
                print(f"${unit_price:.2f}")
                print("Quantity:")
                print(f"{value}")
                print("Total:")
                print(f"${unit_price *  shopping_cart[list(shopping_cart)[i - 1]]:.2f}")
                #gets total quntity
                q += shopping_cart[list(shopping_cart)[i - 1]]
        print("Total items:", q)


#Option 5
def calculate_subtotal(shopping_cart,products):
    subtotal = 0
    #finds the subtotal by adding up all of the prices of the products
    #displays everything currently in the shopping cart
    for i, (product, value) in enumerate(shopping_cart.items(),1):
        #sees whether or not the key from shopping_list is in the products' dictionary
        if product in products:
            #gets the unit price from the products dictionary
            unit_price = products[list(shopping_cart)[i-1]]
            subtotal += (unit_price *  value)
    return subtotal

def get_discount(sub):
    #Checks whether or not the subtotal is greater than or equal to 40
    if sub >= 40:
        return  0.15
    #Checks whether or not the subtotal is greater than or equal to 20 and less than 40
    elif 20 <= sub < 40:
        return 0.10
    #checks whether or not the subtotal is greater than or equal to 10 and less than 20
    elif 10 <= sub < 20:
        return 0.05
    else:
        return 0


#Option 6
def receipt(shopping_cart, products):
    #checks whether or not the cart is empty or not, if it's not empty, then the program will go into this body
    if len(shopping_cart) != 0:
        print("========== RECEIPT ==========")

        #gets the current local date
        from datetime import datetime
        now = datetime.now()
        #Formats the date so that it's the same format as the example
        formatted_now = now.strftime("%m/%d/%Y").replace("/0", "/")
        print("Date:", formatted_now) 

        #lists all of the shopping carts' products and their items
        display_cart(shopping_cart,products)

        #prints the subtotal
        subtotal = calculate_subtotal(shopping_cart, products)
        print("Subtotal:", f"${subtotal:.2f}")
        
        #calls the discount function
        discount = get_discount(subtotal)

        if discount != 0:
            #this calculates the amount of money saved
            saved = discount * subtotal
        else:
            saved = 0
        #this calculates the final amount after the discount was applied
        final = subtotal - saved
        print("Discount: ", f"{discount:.0%}")
        print("Amount Saved: ", f"${saved:.2f}")
        print("Final Total:", f"${final:.2f}")
        print("Thank you for your time shopping here!")
        return True
    #operates if the cart is empty
    else:
        print("You can't check out! You have nothing in your shopping cart")
        return False
    
#control 
checkout = False

#While loop that loops until the customer selects checkout
while checkout == False:
    #Main menu
    print("========== SMART SHOPPING CART ==========")
    print()
    print("1. View Available Products")
    print()
    print("2. Add Product to Cart")
    print()
    print("3. Remove Product from Cart")
    print()
    print("4. View Shopping Cart")
    print()
    print("5. View Current Total")
    print()
    print("6. Checkout")
    print()
    #Asks the user to input their choice based off the menu
    choice = int(input("Enter your choice:"))
 
    #Checks if the user chose option 1
    if choice == 1:
        display_products(products)

    #Checks if the user chose option 2
    elif choice == 2:
        add_product(shopping_cart, products)

    #Checks if the user chose option 3
    elif choice == 3:
        remove_product(shopping_cart)
        
    #Checks if the user chose option 4
    elif choice == 4:
        display_cart(shopping_cart, products)

    #Checks if the user chose option 5
    elif choice == 5:
        print("========== SUBTOTAL ==========")
        #this will get the subtotal from the function "calculate_total"
        subtotal = calculate_subtotal(shopping_cart, products)
        print("Subtotal:", f"${subtotal:.2f}")

    #checks if the user chose option 6
    elif choice == 6:
        #this will get the subtotal from the function "calculate_total"
        calculate_subtotal(shopping_cart, products)
        #this will get the checkout from the "receipt" function
        checkout = receipt(shopping_cart, products)
        
    #This function runs when the user chooses a number that's out of the range of 1 and 6 inclusive
    else:
        print("Invalid option!")
