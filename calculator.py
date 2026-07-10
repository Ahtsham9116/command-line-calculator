# ====================================================

# Project: Command line Calculator
# Author: Muhammad Ahtsham Javed
# Language: Python
# version: 1.0

# ====================================================

import math

SEPARATOR = "=" * 43

#======================MENU=========================

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_menu():
    print(SEPARATOR)
    print(" 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Floor Division\n 6.Modulus\n 7.Exponentiation\n 8.Square Root\n 9.Percentage\n 0.Exit\n")


print(SEPARATOR + "\n")
print("   COMMAND LINE CALCULATOR   \n")
while True:
    print(SEPARATOR)
    display_menu()
    choice = get_int_input("Enter your choice: ")
    print(SEPARATOR)

    #==================Validation=========================
    if 0 <= choice <= 9:
        pass     
    #--------------------Addition-----------------------
    
    if choice == 1:
        print("You have selected Addition, please enter two numbers:\n")
        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")
        result = num1 + num2
        print(f"The result of addition is: {result}")
        
    #--------------------Subtraction-----------------------

    elif choice == 2:
        print("You have selected Subtraction, please enter two numbers:\n")
        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
        
    #--------------------Multiplication-----------------------

    elif choice == 3:
        print("You have selected Multiplication, please enter two numbers:\n")
        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
        
    #--------------------Division-----------------------

    elif choice == 4:
        print("You have selected Division, please enter two numbers:\n")
        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = num1 / num2
        print(f"The result of division is: {result}")
        
    #--------------------Floor Division-----------------------

    elif choice == 5:
        print("You have selected Floor Division, please enter two numbers:\n")
        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")
        if num2 == 0:
            print("Error: Floor division by zero is not allowed.")
            continue
        result = num1 // num2
        print(f"The result of floor division is: {result}")
        
    #--------------------Modulus-----------------------

    elif choice == 6:
        print("You have selected Modulus, please enter two numbers:\n")
        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")
        if num2 == 0:
            print("Error: Modulus by zero is not allowed.")
            continue
        result = num1 % num2
        print(f"The result of modulus is: {result}")

    #--------------------Exponentiation-----------------------

    elif choice == 7:
        print("You have selected Exponentiation, please enter the base and exponent:\n")
        base = get_float_input("Enter the base number: ")
        exponent = get_float_input("Enter the exponent number: ")
        result = base ** exponent
        print(f"The result of exponentiation is: {result}")
        
    #--------------------Square Root-----------------------

    elif choice == 8:
        print("You have selected Square Root, please enter a number:\n")
        num = get_float_input("Enter a number: ")
        if num < 0:
            print("Error: Square root of a negative number is not allowed.")
            continue
        result = math.sqrt(num)
        print(f"The square root of {num} is: {result}")
        
    #--------------------Percentage-----------------------

    elif choice == 9:
        print("You have selected Percentage, please enter two numbers:\n")
        num1 = get_float_input("Enter the total number: ")
        num2 = get_float_input("Enter the percentage: ")
        result = (num1 * num2) / 100
        print(f"{num2}% of {num1} is: {result}")
        
    #--------------------Exit-----------------------

    elif choice == 0:
        print("   Thank you for using the Calculator.   ")
        print("   Have a great day!   \n")

        break
    else:
        print("Invalid choice. Please select a valid option from the menu.\n")
        continue
    
    print(SEPARATOR + "\n")
    continue_choice = input("Do you want another calculation? (y/n): ").lower()
    if continue_choice != "y":
        print("   Thank you for using the Calculator.   ")
        print("   Have a great day!   \n")
        break
    