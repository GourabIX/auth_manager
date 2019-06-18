# ================================================================================================================================================================= #
# PassMaester IS A PASSWORD GENERATOR AND MANAGER HAS BEEN BREWED WITH A LOT OF LOVE BY GOURAB SARKAR. IT USES A COMPLEX MIX OF STRONG POTIONS                     #
# THAT GENERATE ALOHOMORA - SAFE (CRYPTOGRAPHICALLY SECURE) PASSWORDS AND STORES THEM FOR YOU.                                                                      #                                  #
#                                                                                                                                                                   #
# THIS PROGRAM ALONG WITH IT'S COMPLETE SOURCE CODE IS FREE TO USE, MODIFY AND DISTRIBUTE. I WOULD ONLY REQUEST YOU, THE USER, TO                                   # 
# INCLUDE A CREDIT TO MY NAME WHEN YOU DO:                                                                                                                          #
# MADE WITH LOVE BY GOURAB SARKAR (https://github.com/GourabIX)                                                                                                     #
# ================================================================================================================================================================= #


# GRAB PassMaester's FRIENDS
import csv
from secure import *
import os

# MODULE DEFINITION TO WRITE DATA TO CSV FILE
def write_pwd(user_pref, site, acc_id, pass_wd):

    if user_pref == "y":
        entry_point(69)                                                                 # DECRYPT FILE FIRST
        with open("engine/say_shazam.csv", "a") as secret_csv:
            csv_wr = csv.writer(secret_csv)
            csv_wr.writerows([[site, acc_id, pass_wd]])
        secret_csv.close()
        print("Data securely stored and saved. Only YOU know how to access it.")
        entry_point(49)                                                                 # ENCRYPT THE UPDATED FILE

    elif user_pref == "n":
        print("As you wish. But remember that the passwords will get lost forever the moment you close the command console.")
    
    else:
        print("You pressed a wrong key. Please try again.")

def purger():

    # CLEAN UP REDUNDANT DATA
    if os.path.exists("./engine/say_shazam.csv"):
        os.remove("./engine/say_shazam.csv")

def open_vault():
    with open("engine/say_shazam.csv", 'r') as secret_csv:
        csv_rdr = csv.reader(secret_csv)
        for row in csv_rdr:
            if row != []:
                print("|--------------------------------------------------------|")
                site, account_id, password = row[0], row[1], row[2]
                print(" Site URL :", str(site), "\n Account ID :", str(account_id), "\n Password :", str(password))
    print("|--------------------------------------------------------|")
    secret_csv.close()

def exit_action():                                                  # INITIATES CLEANUP IF EXIT IS ABRUPT
    print("\nCleaning up Redundant data before exiting...")
    purger()
