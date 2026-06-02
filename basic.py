from pathlib import Path
import time
import os

print("Zee was here.")

time.sleep(1)

rbxcookiespath = f"{os.path.expanduser("~")}\\AppData\\Local\\Roblox\\LocalStorage\\RobloxCookies.dat"

def clear_roblox_cookies():
    with open(rbxcookiespath, "w") as f:
        f.seek(0)
        f.truncate()
    print("Cleared Cookies")
    return


menu = """
Note: This is the basic version of the menu, in the future I will add the verison with cloud/local account saves (when I get the time).

01: Clear Roblox App Cookies

99: Exit
"""

print(menu)

while True:
    option = int(input(": "))
    if option == 1:
        clear_roblox_cookies()
    
    if option == 99:
        exit(1)
