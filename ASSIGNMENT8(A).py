# Program 1: Lottery
import random

import shutil
# colors for fonts
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WHITE = '\033[0m'
    FAIL = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[1;36;40m'
    BOLD =  '\033[1m'
columns = shutil.get_terminal_size().columns 
# fuction for range
def winningNumber():
    return sorted(random.sample(range(0,10), 3))
# function to enter lucky number
def userInt():
    userInput = []
    for i in range(3):
        print("◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️")
        inputLotto = int(input(bcolors.YELLOW + bcolors.BOLD + "Lucky Number [0-9]: " + bcolors.WHITE))
        if 0 <= inputLotto <= 9:
            userInput.append(inputLotto)
        else:
            input(bcolors.FAIL+ "Invalid! Please enter lucky number range from 0-9. Press enter to continue..."+ bcolors.WHITE)
            inputLotto = int(input(bcolors.YELLOW + bcolors.BOLD + "Lucky Number [0-9]: " + bcolors.WHITE))
            userInput.append(inputLotto)
    return sorted(userInput)

# function that has consitional statements that displays if you win or lose
def checker(userInput, wins):

    if userInput == wins:
        print (bcolors.YELLOW + "3️⃣   / 9️⃣   Lotto Result Today" .center(columns) + bcolors.WHITE)
        print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)
        print (bcolors.YELLOW + "🎉  🎉  🎉  YOU WON!  🎉  🎉  🎉".center(columns)+ bcolors.WHITE)
        print (bcolors.YELLOW + "You can claim your prize at our local lotto outlet." .center(columns) + bcolors.WHITE)
        print (bcolors.HEADER +  bcolors.BOLD +  f"LOTTO RESULT : {wins}".center(columns) + bcolors.WHITE)
        print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)
        print (bcolors.OKBLUE + bcolors.BOLD + "YOUR LUCKY NUMBERS:".center(columns) + bcolors.WHITE)
        print (bcolors.OKBLUE + bcolors.BOLD + f"{userInput}".center(columns) + bcolors.WHITE)
        print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)
    else:
        print (bcolors.YELLOW + "3️⃣   / 9️⃣   Lotto Result Today" .center(columns) + bcolors.WHITE)
        print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)
        print (bcolors.FAIL + " ☹   ☹   ☹  YOU LOSE! ☹   ☹   ☹".center(columns)+ bcolors.WHITE)
        print (bcolors.FAIL + "Try again your luck." .center(columns) + bcolors.WHITE)
        print (bcolors.HEADER +  bcolors.BOLD + f"LOTTO RESULT : {wins}".center(columns) + bcolors.WHITE)
        print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)
        print (bcolors.OKBLUE + bcolors.BOLD + "YOUR LUCKY NUMBERS:".center(columns) + bcolors.WHITE)
        print (bcolors.OKBLUE + bcolors.BOLD + f"{userInput}".center(columns) + bcolors.WHITE)
        print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)

def main():
    userInput = userInt()
    wins= winningNumber()
    checker(userInput, wins)
# Function to start the game 
def menu():
    print ()
    print(bcolors.YELLOW + "🎰   LOTTERY GAME   🎰".center(columns) + bcolors.WHITE)
    print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)
    print (bcolors.HEADER +  bcolors.BOLD +"MENU".center(columns) + bcolors.WHITE)
    print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)
    print ("👋".center(columns))
    print (bcolors.YELLOW + "Hello! Welcome to 3/9 Lotto!".center(columns) + bcolors.WHITE)
    print ()
    print (bcolors.HEADER + "HOW TO PLAY 3/9 Lotto?".center(columns) + bcolors.WHITE)
    print ("In this game, you must input your lucky number from 0 to 9. You will be awarded if you correctly guess the winning number.".center(columns) )
    print ()
    print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)
    print (" 💜 I wish you luck! 💜 ".center(columns) )
    print ("🍀".center(columns))
    print (bcolors.YELLOW +"Press 0 to start the game".center(columns)+ bcolors.WHITE)
    print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)  
    t = True
    while t:
        print("◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️")
        option = input(bcolors.BOLD + bcolors.OKGREEN +"Enter 0 to start: " + bcolors.WHITE)
        print("◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️")
        if option == '0':
            print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)
            print ()
            print ("🎰  🎰  🎰".center(columns))
            print (bcolors.YELLOW + "     3️⃣   / 9️⃣   Lotto game" .center(columns) + bcolors.WHITE)  
            t = False
            main()
        else:
            input(bcolors.FAIL+ "Invalid input. Press ENTER to continue..."+ bcolors.WHITE)
            print("◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️")
menu()
# loop to restart the game
while True:
    while True:
        print("◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️")
        restart = input("Would you like to restart the game? 🟡 YES or 🔴 NO:")
        print("◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️  ◻️")
        if restart in ('yes', 'no', 'YES', 'NO'):
            break
        print("invalid input.")
    if restart == "yes" or restart == "YES":
        print ("... ⏳ ...".center(columns))
        restart = menu()
        continue
    elif restart == "no" or restart == "NO":
        print (bcolors.HEADER + "Thank you for playing!".center(columns) + bcolors.WHITE)
        print ("🔒".center(columns) )
        print(bcolors.FAIL +"END".center(columns) + bcolors.WHITE)
        print (bcolors.CYAN + "--------------------------------------------------------".center(columns)+ bcolors.WHITE)
        break