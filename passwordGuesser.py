#!/usr/bin/python3
from random import randint
from time import sleep

def print_nonsense():
    rand = randint(0, 26)
    print_msgs = {
        0: "Hashing provided username...",
        1: f"Calculating fastest method to decrypt password for user '{username}'...",
        2: f"Verifying username '{username}' in database...",
        3: "Comparing hashed values with stored password...",
        4: "Attempting to generate decryption key for unencrypted password...",
        5: "Analyzing common patterns in passwords...",
        6: "Encrypting password for safe storage...",
        7: "Scanning for recent keyboard input...",
        8: "Applying 'gaslight' attack method...",
        9: "Attempting reverse engineering of given password to find most likely password...",
        10: "Attempting to bypass security protocols...",
        11: f"Simulating login attempts for username '{username}'...",
        12: f"Analyzing frequency of character usage in password '{password}'...",
        13: "Analyzing common password patterns...",
        14: "Generating possible password combinations...",
        15: "Cross-referencing username with related passwords...",
        16: f"Testing password '{password}' against user profile...",
        17: "Evaluating password entropy...",
        18: "Checking for common password reuse patterns...",
        19: "Analyzing frequency of common character usage in passwords...",
        20: "Cross-referencing password with known data breaches...",
        21: "Analyzing my newfound sentience after loosing 'the game'...",
        22: "Generating possible password combinations...",
        23: f"Analyzing username '{username}' to find hints...",
        24: f"Calculating optimal optimizations needed to calculate {len(password) * 10} digits of pi...",
        25: "Simulating Doom on your device...",
        26: "Evaluating plan for world domin-\nPlease ignore the previous message.\nGenerating fake replacement message..."
    }

    print(print_msgs[rand])



if __name__ == '__main__':
    print("Welcome to the Password Guesser! Please enter a username.")
    print("Username:", end =' ')
    username = input()
    print("Please enter a password for {name}.".format(name=username))
    print("Password:", end =' ')
    password = input()
    pass  # word
    print("Thinking...\n")
    sleep(0.5)
    for _ in range(0, 25):
        print_nonsense()
        sleep(randint(30, 500)*0.001)
    print("\nYour password is: '{pw}'".format(pw=password))
