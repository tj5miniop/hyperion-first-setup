# Import Dependencies
import questionary
import os 
import time


# Define Variables
option_1 = "Install Default Apps"
option_2 = "Update System"
option_3 = "Clean System"

def intro():
    print("---- \n Hello! - Welcome to Hyperion! \n----")
    choice = questionary.select(
        "What would you like to do?",
    choices=[option_1, option_2, option_3 ]
    ).ask()
    return choice

# Define Variables
user_choice = intro()
print(user_choice)

# Check Selection
i = 0 
for i in range(5):
    print("")
    i = i +1
time.sleep(2) 
if user_choice == option_1:
    time.sleep(1)
    print("--- Disclaimer - this will install certain apps which I find are useful to me - these include: \n PrismLauncher, Bottles , SteamGridDB etc - \n If you want to install your OWN selection of apps, Use Bazaar: \n (Psst, it should be on your taskbar, the shop icon next to Steam, If not search it up in the Start Launcher)  ")
    os.system("/usr/bin/bash scripts/application_install.sh")
elif user_choice == option_2:
    print("---- Updating system - SUDO PASSWORD IS REQUIRED ----")
    time.sleep(3)
    os.system("sudo bootc update")
else: 
    print("---- Cleaning system - SUDO PASSWORD IS REQUIRED ----")
    time.sleep(3)
    os.system("sudo rpm-ostree cleanup -m")
