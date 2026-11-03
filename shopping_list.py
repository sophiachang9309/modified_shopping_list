#Name: Sophia Chang
#Class: AM

#dictionary called products, which has prodcuts and their prices
products = {
    "Cookies" : 4.0,
    "Milk" : 4.0,
    "Pumpkin pie": 10.0,
    "Hot chocolate" : 3.0,
    "Mint candy" : 2.0
}

#dictionary called shopping_list, which has products and the quantity of each
shopping_cart = {
}

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
    choice = int(input("Enter your choice: "))
 
    #Checks if the user chose option 1
    if choice == 1:
        #iterates through the dictionary to be able to print every single key and value 
        for i, (product,price) in enumerate(products.items(),1):
            print(f"{i}. {product} : ${price:.2f}")

    #Checks if the user chose option 2
    elif choice == 2:
        print("Products")
        #iterates through the dictionary to be able to print every single key 
        for i, (product,price) in enumerate(products.items(),1):
            print(f"{i}. {product}")

        #allows the user to choose which product they'd like to add to their shopping_cart
        product = input("Choose an available product from the list.: ")

        #verifies that the item number chosen is valid
        while product not in products:
            #invalidates the product chosen
            print("That's not a valid product")
            #allows the user to choose which product they'd like to add to their shopping_cart
            product = input("Choose an available product from the list.: ")

        #allows the user to choose how much of a product that they'd like to buy
        unit = int(input(f"How much {product} would you like to add?:"))

        #verifies that the quantity of the product is valid
        while unit <= 0:
            #invalidates the number chosen
            print("That's not a valid number")
            #allows the user to choose how much of a product that they'd like to buy
            unit = int(input(f"How much {product} would you like to add?:"))
        #tells the user what and how much was added to the shopping cart
        print(f"Added {unit} {product} to your shopping cart!")
        #checks whether or not the product was already added to the shopping cart
        if product not in shopping_cart:
            shopping_cart[product] = unit
        #if the product was added already, you add the amount that the user
        else:
            shopping_cart[product] += unit
        #prints the product and how much of that product is in the shopping_cart
        print(f"{product} quantity is now {shopping_cart[product]}.")

    #Checks if the user chose option 3
    elif choice == 3:
        print("Shopping cart")
        #iterates through the dictionary to be able to print every single key 
        for i, (product,quantity) in enumerate(shopping_cart.items(),1):
            print(f"{i}. {shopping_cart} - Quantity: {quantity}")
        remove = input("What item would you like to delete?")



    # #Checks if the user chose option 4
    # elif choice == 4:
    #     display_cart(shopping_cart)

    # #Checks if the user chose option 5
    # elif choice == 5:
    #     print("========== CURRENT TOTAL ==========")
    #     #this will get the subtotal from the function "calculate_total"
    #     subtotal = calculate_total(shopping_cart)
    #     print("Subtotal:", f"${subtotal:.2f}")

    # #checks if the user chose option 6
    # elif choice == 6:
    #     #this will get the subtotal from the function "calculate_total"
    #     subtotal = calculate_total(shopping_cart)
    #     #this will get the checkout from the "receipt" function
    #     checkout = receipt(subtotal, shopping_cart)
        

    # #This function runs when the user chooses a number that's out of the range of 1 and 6 inclusive
    # else:
    #     print("Invalid option!")
 
     

