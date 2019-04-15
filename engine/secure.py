# ================================================================================================================================================================= #
# AUTH_MANAGER IS A PASSWORD GENERATOR AND MANAGER HAS BEEN BREWED WITH A LOT OF LOVE BY GOURAB SARKAR. IT USES A COMPLEX MIX OF STRONG POTIONS                     #
# THAT GENERATE ALOHOMORA - SAFE (CRYPTOGRAPHICALLY SECURE) PASSWORDS AND STORES THEM FOR YOU.                                                                      #                                  #
#                                                                                                                                                                   #
# THIS PROGRAM ALONG WITH IT'S COMPLETE SOURCE CODE IS FREE TO USE, MODIFY AND DISTRIBUTE. I WOULD ONLY REQUEST YOU, THE USER, TO                                   # 
# INCLUDE A CREDIT TO MY NAME WHEN YOU DO:                                                                                                                          #
# MADE WITH LOVE BY GOURAB SARKAR (https://github.com/GourabIX)                                                                                                     #
# ================================================================================================================================================================= #


# GRAB AUTH_MANAGER'S FRIENDS
import pyAesCrypt

# THE FUNDAMENTALS
buff_size = 64 * 1024
secure_key = "@thanosdidnothingwrong45"

''' TODO : UNCOMMENT THESE LINES
# first_run = 0

# if first_run == 0:
#     secure_key = str(input("Enter your new Master Password : \n Note that if you lose this password, you'll lose your soul, coz passwords = soul. "))
#     first_run = first_run + 1

# if first_run > 0:
#     secure_key = str(input("Enter your Master Password to access your Password Vault : "))
#     first_run = first_run + 1
'''

# GET THE ENCRYPTION RUNNING
def encrypt_file():
    print("Encrypting your data...")
    pyAesCrypt.encryptFile("engine/say_shazam.csv", "engine/6ZFOjBhPwG.csv.aes", secure_key, buff_size)
    print("Your passwords have been securely encrypted. \nPROTIP :: KEEP THAT MASTER PASSWORD IN MIND!")

# GET THE DECRYPTION RUNNING
def decrypt_file():
    user_key = str(input("Enter your Master Password to access your Password Vault : "))
    if user_key == secure_key:
        print("Decrypting your data...")
        pyAesCrypt.decryptFile("engine/6ZFOjBhPwG.csv.aes", "engine/say_shazam.csv", secure_key, buff_size)
        print("Your passwords have been securely decrypted. \nPROTIP :: KEEP THAT MASTER PASSWORD IN MIND!")
    else:
        print("THE PASSWORD THAT YOU ENTERED IS INVALID. Please try again.")
        print("The password that was just generated has NOT been added to your vault.")
        exit(9)

def entry_point(crypt_case):
    if crypt_case == 49:
        encrypt_file()
    elif crypt_case == 69:
        decrypt_file()
    else:
        print("What was that?")
