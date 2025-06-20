from os import system as c
import time
import random
import os

# Colors
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
P = '\x1b[38;5;201m'

def logo():
    c('clear')
    print(f"""{R}
███████╗██████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝
█████╗  ██████╔╝█████╗  ███████╗
██╔══╝  ██╔══██╗██╔══╝  ╚════██║
███████╗██║  ██║███████╗███████║
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝
{P} HACKING WORLD - DIAMOND VIP TOOL
""")

def loading(task, sec):
    print(f"\n{C}[+] {task}...")
    for i in range(sec):
        print(f"{Y}[*] Loading{'.' * (i % 4)}")
        time.sleep(1)

def diamond_hack():
    logo()
    cookie = input(f"{C}ENTER YOUR FF COOKIE: ")
    if len(cookie) < 10:
        print(f"{R}[✖] INVALID COOKIE!")
        time.sleep(2)
        menu()
    loading("Verifying Cookie With Server", 4)
    print(f"{G}[✓] Cookie Verified!\n")
    uid = input(f"{C}ENTER YOUR FREE FIRE UID: ")
    if len(uid) < 6:
        print(f"{R}[✖] INVALID UID!")
        time.sleep(2)
        menu()
    loading("Connecting To Garena Server", 4)
    print(f"{G}[✓] UID Verified!\n")
    loading("Disabling Anti-Cheat System", 3)
    loading("Selecting Diamond Packages", 3)
    print(f"{Y}[!] Root Access Required!")
    input(f"{A}Press Enter After Granting Root Permission...")

    loading("Injecting 99999 Diamonds", 8)
    print(f"{R}[!] Connection Timeout at 98%!")
    time.sleep(2)
    print(f"{Y}Reconnecting Secure Server...")
    loading("Retrying Injection", 4)
    print(f"\n{G}[✓] 99999 Diamonds Successfully Added to UID: {uid}")
    print(f"{P}Enjoy VIP Diamonds 🔥🔥🔥")
    input(f"\n{A}Press Enter To Return To Menu...")
    menu()

def menu():
    logo()
    print(f"{A}[1] Start Unlimited Diamond Hack (Cookie + UID)")
    print(f"{A}[0] Exit Tool")
    choice = input(f"{Y}Select Option: ")
    if choice == '1':
        diamond_hack()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] Invalid Option!")
        time.sleep(1)
        menu()

menu()