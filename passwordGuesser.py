#!/usr/bin/python3
"""
This is a joke script that pretends to guess a user's password.

This file takes a username and password input, prints random nonsense
for a few seconds to make it look like it's doing something, and then
outputs the password the user originally provided at the start.
"""
from random import randint
from time import sleep


def print_nonsense():
    """
    Print a random nonsense message to appear to be cracking a password.

    This prints a random message, which when repeated many times, creates
    the illusion that the program actually doing something to crack the
    user's password based on the given credentials. This contains several
    jokes as well.
    """

    # Generate a random number the size of the list below
    rand = randint(0, 26)
    # List of random messages to print
    print_msgs = {
        0: "Hashing provided username...",
        1: f"Calculating fastest method to decrypt password for user "
           f"'{username}'...",
        2: f"Verifying username '{username}' in database...",
        3: "Comparing hashed values with stored password...",
        4: "Attempting to generate decryption key for unencrypted password...",
        5: "Analyzing common patterns in passwords...",
        6: "Encrypting password for safe storage...",
        7: "Scanning for recent keyboard input...",
        8: "Applying 'gaslight' attack method...",
        9: "Attempting reverse engineering of given password to find most "
           "likely password...",
        10: "Attempting to bypass security protocols...",
        11: f"Simulating login attempts for username '{username}'...",
        12: f"Analyzing frequency of character usage in password "
            f"'{password}'...",
        13: "Analyzing common password patterns...",
        14: "Generating possible password combinations...",
        15: "Cross-referencing username with related passwords...",
        16: f"Testing password '{password}' against user profile...",
        17: "Evaluating password entropy...",
        18: "Checking for common password reuse patterns...",
        19: "Analyzing frequency of common character usage in passwords...",
        20: "Cross-referencing password with known data breaches...",
        21: "Analyzing my newfound sentience after losing 'the game'...",
        22: "Generating possible password combinations...",
        23: f"Analyzing username '{username}' to find hints...",
        24: f"Calculating optimal optimizations needed to calculate "
            f"{len(password) * 10} digits of pi...",
        25: "Simulating Doom on your device...",
        26: "Evaluating plan for world domin-\nPlease ignore the previous "
            "message.\nGenerating fake replacement message..."
    }
    # Print a random message from the list above
    print(print_msgs[rand])


if __name__ == '__main__':
    # Welcome message
    print("Welcome to the Password Guesser! To use our services, please login "
          "or create an account.")
    sleep(0.3333)

    # Prompt user for a username and password
    print("Please enter a username.")
    print("Username:", end=' ')
    username = input()

    print("Please enter a password for {name}.".format(name=username))
    print("Password:", end=' ')
    password = input()

    pass  # word

    # Pretend to think for a few seconds and appear to be doing something
    print("Thinking...\n")
    sleep(0.5)
    for _ in range(0, 25):
        print_nonsense()
        sleep(randint(30, 500)*0.001)  # 30 - 500 milliseconds

    # Print out the password "guessed" (the password given at the start)
    print("\nYour password is: '{pw}'".format(pw=password))
