'''
This project, created by me (Rohan), is designed to be adaptable 
based on user needs. Currently, it functions as a user input system.
'''

import time  # Importing the time library for delay

print("Time has been imported.")  # Checking if the time library has been imported.
time.sleep(2)  # 2-second delay

user_name = input("What is your name? \n")  # Asking for the user's name
print(f"Your name is {user_name}.")  # Printing the user's given name

user_age = input("Alright, what's your age? \n")  # Asking for the user's age
print(f"Okay, your age is {user_age}, understandable.")  # Printing the user's given age

friend_age = input("May I know your friend's age? \n")  # Asking for the friend's age
print(f"Okay, your friend's age is {friend_age}.")  # Printing the friend's age

if user_age > friend_age:  # Checking if the user's age is greater than the friend's age
    print("You are older than your friend!")
elif user_age == friend_age:  # Checking if the user's age is equal to the friend's age
    print("You both are the same age!")
else:
    print("You are younger!")
time.sleep(2)
print("Bye-bye!")  # Farewell message