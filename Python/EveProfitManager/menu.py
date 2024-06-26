from colorama import Fore
import os
from abyss import *
from incursion import *
from testing import *

def menu(startloop="False"):
    while startloop != True:
        menu_text = f"""{Fore.RED}
 ██▓███   ██▀███   ▒█████    █████▒██▓▄▄▄█████▓    ███▄ ▄███▓ ▄▄▄       ███▄    █  ▄▄▄        ▄████ ▓█████  ██▀███  
▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▓██   ▒▓██▒▓  ██▒ ▓▒   ▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ ▒████▄     ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒▒████ ░▒██▒▒ ▓██░ ▒░   ▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░░▓█▒  ░░██░░ ▓██▓ ░    ▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░░▒█░   ░██░  ▒██▒ ░    ▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░  ▒ ░   ░▓    ▒ ░░      ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░  ░      ▒ ░    ░       ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
░░         ░░   ░ ░ ░ ░ ▒   ░ ░    ▒ ░  ░         ░      ░     ░   ▒      ░   ░ ░   ░   ▒   ░ ░   ░    ░     ░░   ░ 
            ░         ░ ░          ░                     ░         ░  ░         ░       ░  ░      ░    ░  ░   ░     
{Fore.GREEN}
1. Abyss Money Tracker
2. Incursion Tracker
3. Testing 

    Choice: {Fore.RED}"""
        try:
            user_input = input(menu_text)
        except ValueError:
            os.system("CLS")
            print(f"\n{Fore.RED}Invalid choice. Please enter 1 or 2.")
            continue

        if user_input == "1":
            os.system("CLS")
            abyssMain()
            # startloop = True #This will fully end the loop after pressing to not track anymore abyss runs.
        
        elif user_input == "2":
            os.system("CLS")
            incursion()
        
        elif user_input == "3":
            os.system("CLS")
            testing()

        elif user_input.upper() == "Q":
            print("\n    goodbye\n")
            break  # Exit the loop and end the program

        else:
            os.system("CLS")
            print(f"\n{Fore.RED}Invalid choice. Please enter 1 or 2.")
