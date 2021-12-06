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
columns = shutil.get_terminal_size().columns

print(bcolors.HEADER + "GUESS THE NUMBER GAME".center(columns) + bcolors.WHITE )
print()
print(bcolors.OKGREEN +"START".center(columns) + bcolors.WHITE)
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
        random = integer.randomInteger()
        print(bcolors.OKBLUE + f"\nGuess the randomly generated number from {integer.lower} to {integer.higher}." + bcolors.WHITE)
    # conditional statements that decide whether your input number is correct.
        chances = 0
        while True:
            guess = int(input("\nEnter your guessed number: "))
            if guess == random:
                print(bcolors.YELLOW + f"\nCongratulations! You got it in {chances + 1} chance{'s' if chances > 1 else ''}!" + bcolors.WHITE)
                print(bcolors.OKGREEN + f"The correct number is {random}." + bcolors.WHITE)
                break
            elif guess < random:
                print(bcolors.FAIL + "Opps! You guessed too small!" + bcolors.WHITE)
            else:
                print(bcolors.FAIL + "Opps! You guessed too high!" + bcolors.WHITE)
            chances += 1


# launching the game
GuessTheNumber = GuessTheNumber()
GuessTheNumber.start()

# loop to restart the game
def Loop():
    print (52 * "-")
    restart = input("Would you like to restart the game? yes or no: ")
    if restart == "yes" or restart == "YES":
        Loop(GuessTheNumber.start())
    if restart == "no" or restart == "NO":
        print (bcolors.HEADER + "Thank you for playing!".center(columns) + bcolors.WHITE)
        print(bcolors.FAIL +"END".center(columns) + bcolors.WHITE)
        

Loop()