from IPython.display import clear_output

active = True
while active: 
    # ask user for calculation to be performed
    list = ['add', 'subtract', 'multiply', 'divide', 'quit']
    
    check_input = True
    while check_input:
        operation = input("Would you like to add/subtract/multiply/divide/quit? ").lower()
        if operation not in list:
            clear_output()
            print("Sorry, but '{}' is not an option.".format(operation))
        else:
            check_input = False
    
    
    if operation == "quit":
        clear_output()
        print("Thank you for using my calculator program!")
        active = False
        break
    
    clear_output()
    
    print("You chose {}.".format(operation))
        
    # this alerts user that order matters for subtracting and dividing
    if operation == "subtract" or operation == "divide":
        print("Please keep in mind that the order of your numbers matter.")
            
    check_input = True
    while check_input:
        try:
            num1 = input("What is the first number? ")
            num2 = input("What is the second number? ")
            num1, num2 = int(num1), int(num2)
            check_input = False
        except:
            clear_output()
            print("You did not type in a number. Please try again.")
    
    clear_output()
    print("First Number: {}".format(str(num1)))
    print("Second Number: {}".format(str(num2)))
    
    # converts numbers input from string to floats
    num1, num2 = float(num1), float(num2)
    
    # asks user if they want to reverse order of numbers if order is not correct when subtracting or dividing
    while operation == "subtract" and num1 < num2:
        ans = input("Would you like to reverse the numbers? Y/N: ").lower()
        if ans == "y":
            num1, num2 = num2, num1
            print("The numbers have been reversed.")
            break
        elif ans == "n":
            print("Numbers not reverse.")
            break
        else:
            print("{} is not an option".format(ans))

    while operation == "divide" and num1 < num2:
        ans = input("Would you like to reverse the numbers? Y/N: ").lower()
        if ans == "y":
            num1, num2 = num2, num1
            print("The numbers have been reversed.")
            break
        elif ans == "n":
            print("Numbers not reversed.")
            break
        else:
            print("{} is not an option".format(ans))

    if operation == "add":
        result = num1 + num2
        print("{} + {} = {}".format(num1, num2, result))
    elif operation == "subtract":
        result = num1 - num2
        print("{} - {} = {}".format(num1, num2, result))
    elif operation == "multiply":
        result = num1 * num2
        print("{} * {} = {}".format(num1, num2, result))
    elif operation == "divide":
        result = num1 / num2
        print("{} / {} = {}".format(num1, num2, result))