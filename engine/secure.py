# ================================================================================================================================================================= #
# AUTH_MANAGER IS A PASSWORD GENERATOR AND MANAGER HAS BEEN BREWED WITH A LOT OF LOVE BY GOURAB SARKAR. IT USES A COMPLEX MIX OF STRONG POTIONS                     #
# THAT GENERATE ALOHOMORA - SAFE (CRYPTOGRAPHICALLY SECURE) PASSWORDS AND STORES THEM FOR YOU.                                                                      #                                  #
#                                                                                                                                                                   #
# THIS PROGRAM ALONG WITH IT'S COMPLETE SOURCE CODE IS FREE TO USE, MODIFY AND DISTRIBUTE. I WOULD ONLY REQUEST YOU, THE USER, TO INCLUDE A CREDIT                  #
# TO MY NAME WHEN YOU DO:                                                                                                                                           #
# MADE WITH LOVE BY GOURAB SARKAR (https://github.com/GourabIX)                                                                                                     #
# ================================================================================================================================================================= #


# GRAB PassMaester's FRIENDS
import pyAesCrypt
import os
import hashlib

# THE FUNDAMENTALS
buff_size = 64 * 1024

def secure_session():

    if os.path.exists("./engine/secure_key"):
        with open("engine/secure_key", "r") as skey_rd:
            secure_key = skey_rd.readline()
            secure_key = secure_key.rstrip()
        skey_rd.close()
        return secure_key

    else:
        with open("engine/secure_key", "w") as skey_wr:
            skey_wr_in = str(input("Please enter your new Master Password. Make sure it's something that's hard to guess for others, but easy for you to remember: \n"))
            hash_obj = hashlib.sha256(skey_wr_in.encode())
            hashed = hash_obj.hexdigest()
            skey_wr.writelines(hashed)
        skey_wr.close()
        return hashed.rstrip()

# GET THE ENCRYPTION RUNNING
def encrypt_file():

    secure_key = secure_session()
    
    if os.path.exists("./engine/say_shazam.csv"):
        print("Encrypting your data...")
        pyAesCrypt.encryptFile("engine/say_shazam.csv", "engine/6ZFOjBhPwG.csv.aes", secure_key, buff_size)
        print("Your passwords have been securely encrypted. \nPROTIP :: KEEP THAT MASTER PASSWORD IN MIND!")
    else:
        pass

# GET THE DECRYPTION RUNNING
def decrypt_file():

    secure_key = secure_session()
    
    user_key = str(input("Enter your Master Password to access your Password Vault : "))
    # ENCODE USER ENTERED MASTER PASSWORD IN SHA-256
    hash_obj = hashlib.sha256(user_key.encode())
    hashed = hash_obj.hexdigest()

    if hashed == secure_key:
        if os.path.exists("./engine/6ZFOjBhPwG.csv.aes"):
            print("Decrypting your data...")
            pyAesCrypt.decryptFile("engine/6ZFOjBhPwG.csv.aes", "engine/say_shazam.csv", secure_key, buff_size)
            print("Your passwords have been securely decrypted. \nPROTIP :: KEEP THAT MASTER PASSWORD IN MIND!")
        else:
            print("We did not find the secure database that contained your saved passwords. If this is your first run, this is normal.")
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
