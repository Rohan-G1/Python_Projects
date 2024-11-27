'''
This Python program, created by me (Rohan), checks if a number is prime. 
It is a basic program using loops and conditionals, ideal for beginners.
The logic is simple and can be easily adapted for more advanced applications.
'''
#-------------------------------------------------------------------------------------------
user_number = int(input("Enter a number: ")) # Get user input
#-------------------------------------------------------------------------------------------
is_prime = True # Assume the number is prime
#-------------------------------------------------------------------------------------------
if user_number <= 1: # Numbers less than or equal to 1 are not prime
    is_prime = False # Declare False if above condition is met
else: # If condition is not met
    for i in range(2, user_number): # Check each number from 2 to just below the user_number
        if user_number % i == 0: # If user_number is divisible by i, it's not prime
            is_prime = False # Declare False if above condition is met
            break # Exit the loop
#-------------------------------------------------------------------------------------------
# Print the final result
if is_prime: # If is_prime condition is met
    print(user_number, "is a prime number.")
else: # If is_prime condition is not met
    print(user_number, "is not a prime number.")
#-------------------------------------------------------------------------------------------