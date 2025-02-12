from os import system, name
import secrets
from subprocess import run

# Global variables
global characters
global password
characters = str()

def n_characters():
    global l
    l = int(input())


def set_characters(use_upper, use_lower, use_numbers, use_special):
    global characters
    characters = ""

    if use_upper:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lower:
        characters += "abcdefghijklmnopqrstuvwxyz"
    if use_numbers:
        characters += "1234567890"
    if use_special:
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

        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 4):
            break
        return password


def password_copy():

    if name == 'nt': # Windows
        run("clip", input=password, text=True, shell=True)

    else: # Linux or macOS
        run("xclip -selection clipboard", input=password, text=True, shell=True)