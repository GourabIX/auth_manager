# ================================================================================================================================================================= #
# AUTH_MANAGER IS A PASSWORD GENERATOR AND MANAGER HAS BEEN BREWED WITH A LOT OF LOVE BY GOURAB SARKAR. IT USES A COMPLEX MIX OF STRONG POTIONS                     #
# THAT GENERATE ALOHOMORA - SAFE (CRYPTOGRAPHICALLY SECURE) PASSWORDS AND STORES THEM FOR YOU.                                                                      #                                  #
#                                                                                                                                                                   #
# THIS PROGRAM ALONG WITH IT'S COMPLETE SOURCE CODE IS FREE TO USE, MODIFY AND DISTRIBUTE. I WOULD ONLY REQUEST YOU, THE USER, TO                                   # 
# INCLUDE A CREDIT TO MY NAME WHEN YOU DO:                                                                                                                          #
# MADE WITH LOVE BY GOURAB SARKAR (https://github.com/GourabIX)                                                                                                     #
# ================================================================================================================================================================= #


# GRAB AUTH_MANAGER'S FRIENDS
import csv

# MDOULE DEFINITIONS TO WRITE DATA TO CSV FILE
def write_pwd_hvp(user_pref, site, pwd_list):

    if user_pref == "y":
        with open("engine/say_shazam.csv", "a") as secret_csv:
            csv_wr = csv.writer(secret_csv)
            csv_wr.writerows([[site, *pwd_list]])
        secret_csv.close()
        print("Data securely stored and saved. Only YOU know how to access it.")

    elif user_pref == "n":
        print("As you wish. But remember that the passwords will get lost forever the moment you close the command console.")
    
    else:
        print("You pressed a wrong key. You know what happens now.")            # IMITTATES DUOLINGO MEME

def write_pwd_pgp(user_pref, site, pgp):

    if user_pref == "y":
        with open("engine/say_shazam.csv", "a") as secret_csv:
            csv_wr = csv.writer(secret_csv)
            csv_wr.writerows([[site, pgp]])
        secret_csv.close()
        print("Data securely stored and saved. Only YOU know how to access it.")

    elif user_pref == "n":
        print("As you wish. But remember that this password will get lost forever the moment you close the command console.")
    
    else:
        print("You pressed a wrong key. You know what happens now.")            # IMITTATES DUOLINGO MEME
