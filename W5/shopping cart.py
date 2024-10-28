
print("Welcome to the shopping cart program!")
print()

# You need to move options and variable where you ask option into the loop

shopping_cart = []
prices = []

# You need create the option variable within while loop to have chance do option != 5
option = None

# you need only check if option not 5, you don't need check if option not "Quit"
while option != 5:
    print("""
      Please select one of the following:
      ...................................
      1. Add item
      2. View Cart
      3. Remove item
      4. Compute total 
      5. quit

      """)
    
    option = int(input("please enter an action: "))

    if option == 1:
        item = input("\nWhat item would you like to add? ")
        shopping_cart.append(item)
        price = float(input(f"\nWhat is the price of '{item}' ? "))
        prices.append(price)
        print(f"\n'{item}' has been to the cart. ")


    elif option == 2:
        print("\nThe contents of the shopping cart ar: ")
        for item in range(len(shopping_cart)):
            print(f"\n{item+1}. {shopping_cart[item]} - ${prices[item]:.2f} ")

    elif option == 3:
        # first line is good
        remove_item = int(input("\nPlease, which item would you like to remove? ")) - 1
        # you need to check if user wrote a number in list range
        if remove_item < 0 or remove_item >= len(shopping_cart):
            print('Invalid index. Please enter a number between 0 and', len(shopping_cart) - 1)
        else:
        # you need to use pop function, not del
            shopping_cart.pop(remove_item)
            prices.pop(remove_item)
            print('Item removed.')

    elif option == 4:
        sum = 0
        for number in prices:
            sum += number
        print(f"\nThe total price of the item in the shopping cart is $ {sum:.2f}")    

        option = int(input("\nPlease enter an action: "))
    else:
        print("\nThank you Goodbye")   