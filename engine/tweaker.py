# ============================================================================================================================================= #
# THIS PASSWORD MANAGER HAS BEEN BREWED WITH A LOT OF LOVE BY GOURAB SARKAR. IT USES A COMPLEX MIX OF STRONG POTIONS THAT GENERATE              #
# ALOHOMORA - SAFE (CRYPTOGRAPHICALLY SECURE) PASSWORDS AND STORES THEM FOR YOU.                                                                #
#                                                                                                                                               #
# THIS PROGRAM ALONG WITH IT'S COMPLETE SOURCE CODE IS FREE TO USE, MODIFY AND DISTRIBUTE. I WOULD ONLY REQUEST YOU, THE USER, TO               # 
# INCLUDE A CREDIT TO MY NAME WHEN YOU DO:                                                                                                      #
# MADE WITH LOVE BY GOURAB SARKAR (https://github.com/GourabIX)                                                                                 #
# ============================================================================================================================================= #


# GRAB PassMaester's FRIENDS
import string
import random
from hvp import gen_hvp
from secure import *
from imprint import *
import os

# MODULE DEFINITION
def pass_customizer(length, sym_en, char_en, num_en, site, acc_id):

    # DECIDE CONFIGURATIONS AND HUMANIZE
    if sym_en == 1:
        sym_en = "Yes"
    else:
        sym_en = "No"

    if char_en == 1:
        char_en = "Yes"
    else:
        char_en = "No"

    if num_en == 1:
        num_en = "Yes"
    else:
        num_en = "No"

    # FEEDBACK SELECTED PASSWORD GENERATOR CONFIGURATION
    print("Password params selected >>")
    print("Length =", length, "; Symbols enabled :", sym_en, "; Characters enabled :", char_en, "; Numbers enabled :", num_en, ".")
    
    # CALL THE HIGH VALUE PASSWORD GENERATOR >>>
    err_status = gen_hvp(length, sym_en, char_en, num_en, site, acc_id)
    if err_status != 0:
        print("Hey! Seems something went off the rails. Maybe try again?")

    purger()                # PURGE ALL REDUNDANT DATA FILES

    # RETURN ERROR_CODE
    return 0
