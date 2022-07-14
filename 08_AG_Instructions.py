# Functions go here

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")
            print()


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print('''Welcome to Addition Quiz this is how you play.
    
    - Choose how many questions you wnat or press <enter>
    for continuous mode.

    - Every question generates two random numbers for you to 
    figure out the answer.

    - When you enter your answer it will tell you
    if you got it wrong or right.

    - When you finish all your questions your game summary is 
    shown at the end.

    Enjoy !!!!!!!''')
    print()

    return""

# Main Routine goes here
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print("Program Continues")