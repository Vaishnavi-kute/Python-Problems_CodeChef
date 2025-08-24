def calculatorDisplay():
    
    display = """Welcome to Calculator
    
Choose one operation:
1. Add
2. Subtract
3. Exit
"""
    return(display)


# Solution as follows
def calculatorFunction(user_choice):
    if user_choice == 1:
        return("Let's initiate addition")
    elif user_choice == 2:
        return("Let's initiate subtraction")
    else:
        return("Exit the program")
    

if __name__ == '__main__':
    print(calculatorDisplay())
    user_choice = int(input("Select the operation: "))
    value = calculatorFunction(user_choice)
    print(value)
