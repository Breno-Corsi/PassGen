from os import system, name
import secrets
from subprocess import run
#import json

# Global variables
global characters
global password
characters = str()

def n_characters():
    global l
    l = int(input())


def set_characters(use_upper, use_lower, use_numbers, use_special):
    global characters

    global c_upper
    global c_lower
    global c_numbers
    global c_special

    c_upper = False
    c_lower = False
    c_numbers = False
    c_special = False

    characters = ""

    if use_upper:
        c_upper = True
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lower:
        c_lower = True
        characters += "abcdefghijklmnopqrstuvwxyz"
    if use_numbers:
        c_numbers = True
        characters += "1234567890"
    if use_special:
        c_special = True
        characters += "!@#^&*"


def get_characters():
    return characters


def generatepassword(l = 12):

    global password
    
    while True:
        if characters == '':
            break
        else:
            password = ''.join(secrets.choice(characters) for i in range(l))

            # Check if password has any upper characters
            if c_upper == True:
                check = False
                while check == False:
                    for c in password:
                        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                            check = True
                            break
                    if check == False:
                        generatepassword(l)

            # Check if password has any lower characters
            if c_lower == True:
                check = False
                while check == False:
                    for c in password:
                        if c in 'abcdefghijklmnopqrstuvwxyz':
                            check = True
                            break
                    if check == False:
                        generatepassword(l)

            # Check if password has any numbers characters
            if c_numbers == True:
                check = False
                while check == False:
                    for c in password:
                        if c in '1234567890':
                            check = True
                            break
                    if check == False:
                        generatepassword(l)

            # Check if password has any special characters
            if c_special == True:
                check = False
                while check == False:
                    for c in password:
                        if c in '!@#^&*':
                            check = True
                            break
                    if check == False:
                        generatepassword(l)

        return password


def password_copy():

    if name == 'nt': # Windows
        run("clip", input=password, text=True, shell=True)

    else: # Linux or macOS
        run("xclip -selection clipboard", input=password, text=True, shell=True)


def store_credential():
    with open('user/Credentials.json', 'wt') as credential_file:
        credential_file.close()
    