# ============================================================================================================================================= #
# THIS PASSWORD MANAGER HAS BEEN BREWED WITH A LOT OF LOVE BY GOURAB SARKAR. IT USES A COMPLEX MIX OF STRONG POTIONS THAT GENERATE              #
# ALOHOMORA - SAFE (CRYPTOGRAPHICALLY SECURE) PASSWORDS AND STORES THEM FOR YOU.                                                                #
#                                                                                                                                               #
# THIS PROGRAM ALONG WITH IT'S COMPLETE SOURCE CODE IS FREE TO USE, MODIFY AND DISTRIBUTE. I WOULD ONLY REQUEST YOU, THE USER, TO               # 
# INCLUDE A CREDIT TO MY NAME WHEN YOU DO:                                                                                                      #
# MADE WITH LOVE BY GOURAB SARKAR (https://github.com/GourabIX)                                                                                 #
# ============================================================================================================================================= #


# GRAB AUTH_MANAGER'S FRIENDS
import string
import random
import csv
from imprint import *

# GENERATE THE PRETTY GOOD PASSWORD
def gen_pgp(site, acc_id):
    
    # POPULATE THE BASE CHARACTERS
    ltr = string.ascii_letters
    dig = string.digits
    sym = "./@#&*"

    # GET BREWING!
    print("Brewing a complex password potion...\n")
    mixer = ltr + dig + sym
    pwd_list = []
    for times in range(random.randint(4, 9)):
        pwd = "".join(map(str, random.sample(mixer, 14)))
        pwd_list.append(pwd)

    # THE PASSWORD THAT LIVED : PASS POTTER
    chosen = random.randint(0, len(pwd_list))
    random.shuffle(pwd_list)
    print("******* YOUR PASSWORD, SERVED HOT! ********")
    print("\n")
    pgp = pwd_list[chosen]
    print(pgp)
    print("\n")

    # DOES MASTER WANT TO SAVE AND ENCRYPT THIS PASSWORD?
    user_pref = str(input("Do you want to save this password? \nIt will be stored securely and will be lost forever if you forget your Master Password. [Y / N] "))
    user_pref = user_pref.lower()
    write_pwd(user_pref, site, acc_id, pgp)

    return 0
