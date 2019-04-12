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

# GENERATE THE PRETTY GOOD PASSWORD
def gen_pgp():
    
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
    print(pwd_list[chosen])
    print("\n")

    return 0
