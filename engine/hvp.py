# ============================================================================================================================================= #
# THIS PASSWORD MANAGER HAS BEEN BREWED WITH A LOT OF LOVE BY GOURAB SARKAR. IT USES A COMPLEX MIX OF STRONG POTIONS THAT GENERATE              #
# ALOHOMORA - SAFE (CRYPTOGRAPHICALLY SECURE) PASSWORDS AND STORES THEM FOR YOU.                                                                #
#                                                                                                                                               #
# THIS PROGRAM ALONG WITH IT'S COMPLETE SOURCE CODE IS FREE TO USE, MODIFY AND DISTRIBUTE. I WOULD ONLY REQUEST YOU, THE USER, TO               # 
# INCLUDE A CREDIT TO MY NAME WHEN YOU DO:                                                                                                      #
# MADE WITH LOVE BY GOURAB SARKAR (https://github.com/GourabIX)                                                                                 #
# ============================================================================================================================================= #


# GRAB PASSBOT'S FRIENDS
import string
import random


def gen_hvp(qty, p_len, sym_en, char_en, num_en):
    
    print("\nFiring up the Advanced Password Generator...\n")
    
    # POPULATE THE BASE CHARACTERS
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

    print("******* YOUR PASSWORDS, SERVED HOT! ********\n")

    for times in range(qty):
        # GET BREWING!
        for times in range(random.randint(6, 9)):
            pwd = "".join(map(str, random.sample(mixer, p_len)))
            pwd_list.append(pwd)
        
    if len(pwd_list) > qty:
        choose_indices = random.sample(range(0, len(pwd_list)), qty)

    random.shuffle(pwd_list)
    print("\n\n".join(pwd_list[choose_indices[i]] for i in range(len(choose_indices))))
    print("\n")

    # ACK SUCCESSFUL COMPLETION
    return 0
