#---------------------------------------------------------------------
#         Menu Driven Application / Function Library
# This application demonstrates how to use a menu to prompt the user  
# for a choice to process. It also demonstrates how the main() and a 
# display_menu() function can be used to test module functions.
#---------------------------------------------------------------------

## Global Constants for the menu choices
ADD_CHOICE = 1
MULTIPLY_CHOICE = 2
FACTORIAL_CHOICE = 3
FACTORIAL_LOOP_CHOICE = 4
QUIT_CHOICE = 5

## Global Variables


## The main function.	
def main():
    # The user's choice variable controls the loop and
    # holds the user's menu choice.
    choice = 0

    while choice != QUIT_CHOICE:
        # Display the choice menu
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))
        
        # Perform the selected action.
        if choice == ADD_CHOICE:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print('The result =', add(num1 , num2))
        elif choice == MULTIPLY_CHOICE:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print('The result =', multiply(num1 , num2))
        elif choice == FACTORIAL_CHOICE:
            num1 = float(input("Enter number: "))
            print('The result =', factorial(num1))
        elif choice == FACTORIAL_LOOP_CHOICE:
            num1 = float(input("Enter number: "))
            print('The result =', factorial_loop(num1))    
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')

			
				
			
			
#----------------------------------------------------------------------
# display_menu - Display the user input menu
#
#   Example call:
#     display_menu()
#  
def display_menu():
    print('-------------------------------------')
    print('Selection Menu:')
    print('1) Add two numbers')
    print('2) Multiply two numbers')
    print('3) Factorial (recursive) of a number')
    print('4) Factorial (using loop) of a number')
    print('5) Quit')
    print('-------------------------------------')
    return


#---------------------------------------------------------------------
#                         Library Module Functions   
#---------------------------------------------------------------------

# add - Add two numbers and return result
#
#   Example call: 
#     add(20, 35)
#     returns the sum of 20 and 35 (55)
#
def add(num1, num2):
    """
    Returns:
        The sum of two argument numbers.
        add(num1, num2)
        Args:
            num1: first number to add
            num2: second number to add
            
        Example call:
            add(20, 35)
            returns 55

    """
    return num1 + num2


# multiply - Multiply two numbers and return result
#
#   Example call: 
#     multiply(5, 10)
#     returns the product of 5 and 10 (50)
#
def multiply(num1, num2):
    return num1 * num2

	
# factorial - Calculate factorial of a positive integer and return result
#
#   Think Python 6.5 - 6.6 (page 55-57) 
#   Uses recursive function:
#   	0! = 1
#       n! = n*(n - 1)!
#       factorial(n) = factorial(n) * factorial(n -1)
#   Example call: 
#     factorial(4)
#     returns 4! (24)
#
def factorial(num):
    if (num == 0):
        return(1)
    else:
        return num * factorial(num - 1)
    

# factorial_loop - Calculate factorial of a positive integer using 
#                  a while loop and return result
#
#   Example call: 
#     factorial_loop(4)
#     returns 4! (24)
#
def factorial_loop(num):
    result = 1
    while num > 1:
        result = result * num
        num = num - 1
    return result 


#---------------------------------------------------------------------
#                     End Library Module Functions   
#---------------------------------------------------------------------

# Call the main function, only if this file is used as a standalone 
# program to test the library functions. 
# Otherwise, use this module as a function library that can be imported

if __name__ == '__main__':
    main()

