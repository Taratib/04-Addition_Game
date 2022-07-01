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


def num_check(question, low, high):

    error = "Please enter an whole number between 1 and 50\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine does here
how_much = num_check("What is the answer?  ", 0, 50)

print("program continues")

played_before = yes_no("Have you played the game before? ")
print()
if played_before == "no":
    instructions()