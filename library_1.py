#--------
#Libraries_and_Modules
#Graden_Rusk
#Oct21_2021
#--------

import time

#----Functions start here----#
List_1 = [] 
#----Main Code----#
def side_1():
    time.sleep(3)
    print("Can you guess the number I have saved in the computer?")
    try:
        awnser = int(input(">>>" ))
    except:
        print("Number please.")
        side_1()
    if awnser == 5:
        print("Congrats you got it!")
    else:
        print("that is absolutely")
        time.sleep(3)
        print("Wrong!")

option_1 = 5