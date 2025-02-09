from os import system, name
from time import sleep
import string
import secrets
from subprocess import run

def lin():
    print('-'*50)


def title(t = 'TITLE'):
    lin()
    print(t.center(50).upper())


def clearterminal():

    if name == 'nt': #Windows
        system('cls')
    else: #Linux or macOS
        system('clear')


def menu():
    clearterminal()
    title('PASSGEN')
    lin()
    print('1 - Generate new password')
    print('2 - Exit')
    lin()
    choosefunction()


def choosefunction():
    
    while True:
        try:
            choice = int(input('Choose an option: '))
            break

        except ValueError:
            print('Error: value should be an integer between 1 and 2')
            sleep(2)
            return menu()

    if choice == 1:
        clearterminal()
        title('GENERATING PASSWORD')
        lin()
        l = int(input('Length of password: '))
        print(generatepassword(l))

    elif choice == 2:
        clearterminal()
        title('EXITING PROGRAM')
        lin()
        for i in range(0,50):
            print('#', end='', flush=True)
            sleep(0.025)
        clearterminal()

    else:
        print('Error: value should be an integer between 1 and 2')
        return choosefunction()


def generatepassword(l = 12):
    lin()

    characters = string.ascii_letters + string.digits + string.punctuation

    while True:

        password = ''.join(secrets.choice(characters) for i in range(l))

        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 4):
            break

    print('Password copied to your clipboard! [ Cntrl+V ]')

    if name == 'nt': #Windows
        run("clip", input=password, text=True, shell=True)

    else: #Linux or macOS
        run("xclip -selection clipboard", input=password, text=True, shell=True)
    
    return password