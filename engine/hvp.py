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

def gen_hvp(qty, p_len, sym_en, char_en, num_en, site):
    
    print("\nEngaging Advanced Security System Thrusters...\n")
    
    # POPULATE THE BASE CHARACTERS
    otp_flag = 0
    if char_en == "Yes":
        ltr = string.ascii_letters
    else:
        ltr = ""
    
    if num_en == "Yes":
        dig = string.digits
    else:
        dig = ""
    
    if sym_en == "Yes":
        sym = string.punctuation
    else:
        sym = ""

    mixer = ltr + dig + sym
    pwd_list = []

    if ltr == "" and sym == "" and dig != "":
        p_len = 6
        print("Hmm... Your selection indicates that you want to generate numeric only OTPs. Granted!")
        print("******* YOUR OTPs, SERVED HOT! *******\n\n")                                                 # TODO : MAYBE ADD MORE CUSTOMIZABILITY OPTIONS LATER?
                                                                                                            # TODO : ALLOW OTP LENGTH TO BE CUSTOMIZED
        otp_flag = 1

    if otp_flag == 0:
        print("******* YOUR PASSWORDS, SERVED HOT! *******\n")

    for times in range(qty):
        # GET BREWING!
        for times in range(random.randint(6, 9)):
            pwd = "".join(map(str, random.sample(mixer, p_len)))
            pwd_list.append(pwd)
        
    if len(pwd_list) > qty:
        choose_indices = random.sample(range(0, len(pwd_list)), qty)

    random.shuffle(pwd_list)
    # print("\n\n".join(pwd_list[choose_indices[i]] for i in range(len(choose_indices))))
    pwd_list = list(map(str, (pwd_list[choose_indices[i]] for i in range(len(choose_indices)))))
    for pass_wd in pwd_list:
        print(pass_wd, "\n")
    
    # DOES MASTER WANT TO SAVE AND ENCRYPT THIS PASSWORD?
    user_pref = str(input("Do you want to save these passwords? \nIt will be stored securely and will be lost forever if you forget your Master Password. [Y / N] "))
    user_pref = user_pref.lower()
    write_pwd_hvp(user_pref, site, pwd_list)

    # ACK SUCCESSFUL COMPLETION
    return 0
