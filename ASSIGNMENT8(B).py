# Program 2: Guess the number
import random
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WHITE = '\033[0m'
    FAIL = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[1;36;40m'
columns = shutil.get_terminal_size().columns

class GuessTheNumber:

    def __init__(integer):
        # define the range of the game
        integer.lower = 0
        integer.higher = 100

    # code that generate random number
    def randomInteger(integer):
        return random.randint(integer.lower, integer.higher)

    # the core of the game
    def start(integer):
        print ()
        print(bcolors.HEADER + "💜 GUESS THE NUMBER GAME 💜".center(columns) + bcolors.WHITE )
        print()
        print(bcolors.OKGREEN +"  START ".center(columns) + bcolors.WHITE)
        print("🟩".center(columns))
        print("".center(columns))
        random = integer.randomInteger()
        print(bcolors.CYAN + f"\nGuess the randomly generated number from {integer.lower} to {integer.higher}." + bcolors.WHITE)
    # conditional statements that decide whether your input number is correct.
        chances = 0
        while True:
            guess = int(input("\n\033[1;37;40m❔ Enter your guessed number:  \033[0;37;40m"))
            if guess == random:
                print (175 * "-")
                print (" 🎉  🎉  🎉   YOU WON!    🎉  🎉  🎉 ".center(columns))
                print(bcolors.YELLOW + f"\nCongratulations! You got it in {chances + 1} chances!" + bcolors.WHITE)
                print(bcolors.OKGREEN + f"You got it right!!! It's {random}." + bcolors.WHITE)
                break
            elif guess < random:
                print(bcolors.FAIL + "  ⬇️   Opps! You guessed too small!" + bcolors.WHITE)
            else:
                print(bcolors.FAIL + "  ⬆️   Opps! You guessed too high!" + bcolors.WHITE)
                chances += 1



# launching the game
GuessTheNumber = GuessTheNumber()
GuessTheNumber.start()

# loop to restart the game
while True:
    while True:
        print (175 * "-")
        restart = input("Would you like to restart the game? 🟡 YES or 🔴 NO:")
        if restart in ('yes', 'no', 'YES', 'NO'):
            break
        print("invalid input.")
    if restart == "yes" or restart == "YES":
        print ("... ⏳ ...".center(columns))
        print (175 * "-")
        restart = GuessTheNumber.start()
        continue
    elif restart == "no" or restart == "NO":
        print (bcolors.HEADER + "Thank you for playing!".center(columns) + bcolors.WHITE)
        print ("🔒".center(columns) )
        print(bcolors.FAIL +"END".center(columns) + bcolors.WHITE)
        print (175 * "-")
        break
