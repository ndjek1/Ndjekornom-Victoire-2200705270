# Error handling in Python

# Exception handling with try, except, else, and finally
# Custom exceptiion

"""_summary

Error handling in Python helps to handle unexpected situations and errors
1. Try : contains the code that might throw an exception
NB: If an exceptioin occurs the rest of the code in the try block is skipped or ignored
2. Except: catches and handles the exceptions
NB: You can specify different handlers to different exceptions types

3. Else: The code runs if no exception occurs
If no exceptions are raised in the try block it runs

4. Finally: This block runs whether an exception is raised/occures or not 
NB: Used for cleaning up actions

"""

# Example 1 : Handle exceptions with division by zero

# try:
#     number = int(input("Enter a number: "))
#     result = 30/number

# except ValueError:
#     print("Invalidnumber! Please enter valid number")

# except ZeroDivisionError:
#     print("Error! Division by zero is not allowed")
# else:
#     print(f"Result is {result}")

# finally:
#     print("Execution terminated ")

    # Exercise 1: Write a function converts a string to an integer and handle both value error 
    # If the string cannot be converted as an integer and the typeError if input is not a string
    # Use multiple except block to handle these exceptions
    # 
# def integer_conversion():
#     try:
#         number = input("Enter a number: ")

#         int_value = int(number) 

#     except ValueError:
#         print("The number cannot be converted to an integer. Please enter a valid ")    

#     except TypeError:
#         print("The input must be a string")

# integer_conversion()


# Custom exceptions
# Example 2: Exception rised for error in the input, if funds are insufficient

class InsufficientFundError(Exception):

    def __init__(self, balance, amount) :
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to widthdraw {self.amount} with only {self.balance} in account"

def withdraw(balance, amount):
    if amount>balance:
        raise InsufficientFundError(balance,amount)
    return balance-amount
    


try:
    balance = 20000
    amount_to_withdraw = 14000

    new_balance = withdraw(balance,amount_to_withdraw)
except InsufficientFundError as e:
    print(f"Error: {e.message}")

else: 
    print(f"Withdraw successful! New balance: {new_balance}")

finally:
    print("Thank you for choosing our system")

    """
    Defining a custom exceptiion

    Class CustomException(Exceptio):
        Custom Exception for specific error cases

        def __init__(self, message):
        super().__init__(message)
        self.message = message

        Raising a customError ("Value cannot be negative)
        def check_value(number):
            if number<0:
                raise CustomException("Value cannot be negative)

    """


# Exercise 2: Create a custom exception invalid age error and write a function that raise the error if the given age is negative
# Handle this custom exception when calling the function

class NegativeAgeError(Exception):
    def __init__(self,message):
        super().__init__(self,message)
        self.message = message

def check_age(age):
    if age < 0:
        raise NegativeAgeError("You cannot have a negative age")
    return f"You are {age} years old"

try:
    age  = -23

    check_age(age)
except NegativeAgeError as e:
    print("Error:", e.message)
finally:
    print("Execution terminated")