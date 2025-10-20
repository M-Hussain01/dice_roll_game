import random
import time

    
def dice_roll():
    # This is the function defination
    """This game will give a random number 
             Every time you roll the number is random"""
    # This is the into
    print(""" Welcome To The Dice Roll Game

How many dice do you want to roll?
Please enter a number greater than 0
""")
   
    try:
        n = int(input("how many time you roll a dice :"))
        if n != 0:
            print(f"your {n} dice rolling..........\n")
        else:
            print("please write a number upto 0")
    except ValueError:
        print("please enter a number")
        dice_roll()
    else:
        for i in range(1,n+1):
            time.sleep(0.7)
            print(f"The result is for dice number {i} is {random.randint(1,6)}")
    last = input("\nif you want to roll again enter YES\n"
    " and if you want to quit write QUIT : ").lower().strip()
    while True:
        if last == "yes":
            dice_roll()
        elif last == "quit" :
            print("Thanks for playing")
            break
        else:
            print("please enter a valid")
            break
dice_roll()
    




