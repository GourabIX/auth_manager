# ================================================================================================================================================================= #
# AUTH_MANAGER IS A PASSWORD GENERATOR AND MANAGER HAS BEEN BREWED WITH A LOT OF LOVE BY GOURAB SARKAR. IT USES A COMPLEX MIX OF STRONG                             #
# POTIONS THAT GENERATE ALOHOMORA - SAFE (CRYPTOGRAPHICALLY SECURE) PASSWORDS AND STORES THEM FOR YOU.                                                              #                                  #
#                                                                                                                                                                   #
# THIS PROGRAM ALONG WITH IT'S COMPLETE SOURCE CODE IS FREE TO USE, MODIFY AND DISTRIBUTE. I WOULD ONLY REQUEST YOU, THE USER, TO                                   # 
# INCLUDE A CREDIT TO MY NAME WHEN YOU DO:                                                                                                                          #
# MADE WITH LOVE BY GOURAB SARKAR (https://github.com/GourabIX/auth_manager)                                                                                        #
# ================================================================================================================================================================= #


# GRAB AUTH_MANAGER'S FRIENDS
import string
import random
import sys
sys.path.append("C:/Users/gsarkar/Documents/Code/auth_manager/engine")
from hvp import gen_hvp
from pgp import gen_pgp
from tweaker import pass_customizer
from secure import *

# DRESS FOR THE JOB YOU WANT!
print("| -------------------------------------------------------------------- |")
print("|                       Welcome to Auth_Manager!                       |")
print("|                               v 0.1.5                                |")
print("| -------------------------------------------------------------------- |")

# THE MAIN FUNCTION, LITERALLY
if __name__ == '__main__':

    splash = int(input("Hiya There! Enter 0 to generate passwords or 9 to decrypt and access your password vault : "))

    if splash == 0:
        site = str(input("\nEnter the URL for which you want to generate your password: "))
        adv_en = str(input("Now, do you want to enable advanced mode [Y / N] ? "))
        adv_en = adv_en.lower()

        if adv_en == "y":
            # GET THE CONFIG FROM USER
            print("In the next line, enter your password complexity preferences, separated by spaces. ")
            print("Usage : <how_many> <password_length> <symbols_enabled> <characters_enabled> <numerics_enabled> ")
            print("If you want to generate OTPs, enter only <how_many> and <numerics_enabled> fields, and fill the rest with 0.")
            print("Sample entry [1 = enable, 0 = disable] : 6 24 1 1 0")
            qty, length, sym_en, char_en, num_en = map(int, input().split(' '))
            print("Okay... Got your password customisation preferences!\n")
            
            # CALL THE PASSWORD CUSTOMIZER
            print("Brewing some strong Password Potion now...")
            err_status = pass_customizer(qty, length, sym_en, char_en, num_en, site)
            if err_status != 0:
                print("Something went wrong. Sorry for the hiccup. Do Try again!")

        elif adv_en == "n":
            # TODO : DECRYPT FILE FIRST
            err_status = gen_pgp(site)
            if err_status != 0:
                print("Something went wrong. Sorry for the hiccup. Do Try again!")
            entry_point(49)
            # TODO : DELETE CSV FILE FROM DISK
        
        else:
            print("Hmm... You entered a wrong argument. Please, try again! :)")
    
    elif splash == 9:
        # TODO : Deal with Decryption in secure.py
        entry_point(69)                                         # WOW! *NODS IN DISBELIEF; LAUGHS IN entry_point*
    
    else:
        print("What was that? Please try again.")
