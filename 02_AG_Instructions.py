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
    print("**** Welcome to the Addition Quiz ****")
    print()
    print("This is where the rules go.")

    return ""

# Main Routine goes here
played_before = yes_no("Have you played the game before? ")
print()
if played_before == "no":
    instructions()

print("Program continues")