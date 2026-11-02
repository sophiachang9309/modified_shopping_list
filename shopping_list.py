#Name: Sophia Chang
#Class: AM

#dictionary called products, which has prodcuts and their prices
products = {
    "Cookies" : 4.00,
    "Milk" : 4.00,
    "Pumpkin pie": 10.00,
    "Hot chocolate" : 3.00,
    "Mint candy" : 2.00
}

#dictionary called shopping_list, which has products and the quantity of each
shopping_cart = {
    "Cookies" : 25,
    "Milk" : 10,
    "Pumpkin pie": 5,
    "Hot chocolate" : 15,
    "Mint candy" : 20
}

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
        products.items()
        

    #Checks if the user chose option 2
    elif choice == 2:
        add_product(shopping_cart,products)

    #Checks if the user chose option 3
    elif choice == 3:
        remove_product(shopping_cart)

    #Checks if the user chose option 4
    elif choice == 4:
        display_cart(shopping_cart)

    #Checks if the user chose option 5
    elif choice == 5:
        print("========== CURRENT TOTAL ==========")
        #this will get the subtotal from the function "calculate_total"
        subtotal = calculate_total(shopping_cart)
        print("Subtotal:", f"${subtotal:.2f}")

    #checks if the user chose option 6
    elif choice == 6:
        #this will get the subtotal from the function "calculate_total"
        subtotal = calculate_total(shopping_cart)
        #this will get the checkout from the "receipt" function
        checkout = receipt(subtotal, shopping_cart)
        

    #This function runs when the user chooses a number that's out of the range of 1 and 6 inclusive
    else:
        print("Invalid option!")
 
     

