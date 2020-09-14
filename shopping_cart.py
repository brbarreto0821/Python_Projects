from IPython.display import clear_output

# global list variable
cart = []

# create function to add items to cart
def addItem(item):
    clear_output()
    cart.append(item)
    print("{} has been added.".format(item))

# create function to remove items from cart
def removeItem(item):
    clear_output()
    try:
        if item == str(item):
            cart.remove(item)
            print("{} has been removed".format(item))
        else:
            item = cart[item - 1]
            cart.remove(item)
            print("{} has been removed".format(item))
    except:
        print("Sorry we could not remove that item")

# create a function to show items in cart
def showCart():
    clear_output()
    if cart:
        print("Here is your cart:")
        for item in cart:
            index = cart.index(item)
            print("{}) {}".format(index + 1, item))
    else:
        print("Your cart is empty.")
        
# create function to clear items from cart
def clearCart():
    clear_output()
    cart.clear()
    print("Your cart is empty.")

# create main function that loops until the user quits
def main():
    done = False
    
    while not done:
        ans = input("quit/add/remove/show/clear: ").lower()
        
        # base case
        if ans == "quit":
            showCart()
            print("\nThanks for using our program!")
            done = True
        elif ans == "add":
            item = input("What would you like to add? ").title()
            addItem(item)
        elif ans == "remove":
            showCart()
            item = input("What item would you like to remove? ").title()
            if (item == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7"):
                item = int(item)
                removeItem(item)
            else:
                removeItem(item)
        elif ans == "show":
            showCart()
        elif ans == "clear":
            clearCart()
        else:
            print("Sorry that was not an option")

main()