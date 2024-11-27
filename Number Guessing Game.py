'''
Number Guessing Game - Rohan
This project is a simple and engaging number guessing game.
It's designed to be adaptable and can be modified based on user needs. 
Currently, it functions as a user input system where players guess a 
randomly generated number within a specified range.
'''

#------------------------------------
import random  # Importing the random library
import time    # Importing the time library
#------------------------------------
random_number = random.randint(1, 100)  # Setting a range
attempts = 0  # Variable for the number of attempts
#------------------------------------
time.sleep(2)  # 2-second delay
#---------------------------------------------------
print("Welcome to the guessing game!")  # Greeting the user
print("I am thinking of a number between 1 and 100.")
#---------------------------------------------------------------------------------
while True:  # While loop to run the following code until the condition is met
    guess = int(input("Guess a number: "))  # Asking the user to guess a number
    attempts += 1

    if guess > random_number:  # Checking if the guessed number is higher than the generated number
        print("No, your guess is too high!")
    elif guess < random_number:  # Checking if the guessed number is lower than the generated number
        print("No, your guess is too low!")
    else:  # If both the above conditions are not met
        print(f"Good guess! You have guessed the number in {attempts} attempts!")
        break  # Stop the loop
#---------------------------------------------------------------------------------