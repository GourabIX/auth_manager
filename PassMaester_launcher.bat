@echo OFF

REM # ================================================================================================================================================================= #
REM # PassMaester IS A PASSWORD GENERATOR AND MANAGER HAS BEEN BREWED WITH A LOT OF LOVE BY GOURAB SARKAR. IT USES A COMPLEX MIX OF STRONG POTIONS                      #
REM # THAT GENERATE ALOHOMORA - SAFE (CRYPTOGRAPHICALLY SECURE) PASSWORDS AND STORES THEM FOR YOU.                                                                      #                                  #
REM #                                                                                                                                                                   #
REM # THIS PROGRAM ALONG WITH IT'S COMPLETE SOURCE CODE IS FREE TO USE, MODIFY AND DISTRIBUTE. I WOULD ONLY REQUEST YOU, THE USER, TO                                   # 
REM # INCLUDE A CREDIT TO MY NAME WHEN YOU DO:                                                                                                                          #
REM # MADE WITH LOVE BY GOURAB SARKAR (https://github.com/GourabIX)                                                                                                     #
REM # ================================================================================================================================================================= #

pip install pyAesCrypt

start cmd /k python3 PassMaester.py
