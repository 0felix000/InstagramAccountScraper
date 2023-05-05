import time
from time import sleep
from datetime import datetime
import os
from colorama import init, Fore, Back, Style
from tkinter import filedialog
import tkinter as tk
import ctypes
import instaloader
import getpass
cls = lambda: os.system('cls')
root = tk.Tk()
root.withdraw()
init(convert=True)
def ausgabe(x):
    text =  "[" + datetime.now().strftime("%H:%M:%S")+"."+(str(datetime.now().microsecond))[:2] + "]" + " -" + "-"  +  "-" + x
    return text
text = """
 _____ _____   _____                                  _             _____  __     _ _      _____  _____  _____
|_   _|  __ \ /  ___|                                | |           |  _  |/ _|   | (_)    |  _  ||  _  ||  _  |
  | | | |  \/ \ `--.  ___ _ __ __ _ _ __   ___ _ __  | |__  _   _  | |/' | |_ ___| |___  _| |/' || |/' || |/' |
  | | | | __   `--. \/ __| '__/ _` | '_ \ / _ \ '__| | '_ \| | | | |  /| |  _/ _ \ | \ \/ /  /| ||  /| ||  /| |
 _| |_| |_\ \ /\__/ / (__| | | (_| | |_) |  __/ |    | |_) | |_| | \ |_/ / ||  __/ | |>  <\ |_/ /\ |_/ /\ |_/ /
 \___/ \____/ \____/ \___|_|  \__,_| .__/ \___|_|    |_.__/ \__, |  \___/|_| \___|_|_/_/\_\\___/  \___/  \___/
                                   | |                       __/ |
                                   |_|                      |___/
                                """
def scraper():
    cls()
    print(text)
    L = instaloader.Instaloader()
    print()
    print(ausgabe("To Scrape IG Followers, an Account is needed (Hint: Use Burners)"))
    username = input(ausgabe("YOUR IG Username:"))
    password = getpass.getpass(ausgabe("YOUR IG Password (hidden)):"))
    print(ausgabe(Fore.YELLOW + "logging into your account")+ Fore.WHITE)
    try:
        L.login(username,password)
        print(ausgabe("Successfully logged into " + Fore.GREEN + username)+ Fore.WHITE)
    except:
        print(ausgabe("Wrong Mail/Password. Press Enter to get back to the start Menu!"))
        input(ausgabe(">"))
        scraper()

    name = input(ausgabe("Name of the profile to scrape followers:"))
    print(ausgabe("Searching for an Account named " + Fore.GREEN + " " + name + Fore.WHITE + "..."))
    profile = instaloader.Profile.from_username(L.context, name)
    print(ausgabe(Fore.GREEN + "Found " + name + "!")+ Fore.WHITE)
    anz = input(ausgabe("How many accounts do you need?"))
    print(ausgabe("Last of all, in which file do you want your accounts to be saved?"))
    path = filedialog.askopenfilename()
    print(ausgabe(Fore.YELLOW + "Now Scraping " + anz + " Followers of " + name + "!")+ Fore.WHITE)
    follow_list = []
    count = 0
    for followee in profile.get_followers():
        follow_list.append(followee.username)
        file = open(path, 'a')
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        count = count + 1
        if count == int(anz):
            break
    print(ausgabe(Fore.GREEN + anz + " Followers of " + name + " were saved!")+ Fore.WHITE)
    print(ausgabe("Press enter to get back to the main Menu!"))
    input(ausgabe(">"))
    scraper()
ctypes.windll.kernel32.SetConsoleTitleW("IG Account Scraper by 0felix000")
scraper()
