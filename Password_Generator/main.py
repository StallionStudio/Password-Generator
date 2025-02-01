# Imports
import random
import os


# List with letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password_list = []  # Stores all the letters, numbers and symbols in a list
password = ""  # Stores the final password
is_running = True  # Boll to check if the program is running


# Function that clears the terminal
def clear_terminal():
    os.system('cls')


# Function that shows the title
def show_title():
    print("Password - Generator")
    print("--------------------")


# Asks for user input and creates the password
def create_password():
    global password
    global is_running


    num_letters = int(input("How many letters will you have in your password? "))

    num_numbers = int(input("How many numbers will you have in your password? "))

    num_symbols = int(input("How many symbols will you have in your password? "))


    for char in range(0, num_letters):
        password_list.append(random.choice(letters))

    for char in range(0, num_numbers):
        password_list.append(random.choice(numbers))

    for char in range(0, num_symbols):
        password_list.append(random.choice(symbols))

    # Shuffles the password list
    random.shuffle(password_list)

    # Convert the list into a string
    password = ''.join(password_list)

    # Print the password
    print(f"Your password: {password}")

    # Closes the program
    is_running = False


# Main

# Clears the terminal
clear_terminal()

# Main Program
while is_running:
    show_title()
    create_password()
