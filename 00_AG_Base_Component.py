import random

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
    print()

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


def check_rounds():
    while True:
        response = input("How many question: ")

        round_error = "Please type either <enter> or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # stsrt of loop
                if response < 1:
                    print(round_error)
                    continue

            # if response is not an integer go back to
            # start of loop

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine does here
played_before = yes_no("Have you played the game before? ")
print()
if played_before == "no":
    instructions()

rounds_played = 0

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of the Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Question {}".format(rounds_played + 1)

    else:
        heading = "Question {} of {}".format(rounds_played + 1, rounds)

    print(heading)

    num_1 = random.randint(1, 50)
    num_2 = random.randint(1, 50)

    print()
    print("What is {} + {} = ? ".format(num_1, num_2))

    total = num_1 + num_2

    # User input
    users_answer = "Your answer: "
    print()

    choose = input("{} ".format (users_answer))

    # End game if exit code is typed
    if choose == "xxx":
        break

    # Check users answer

    if users_answer == total:
        print("Well done you got it right")
    else:
        print("Sorry you got it wrong. The correct answer was {}".format(total))

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Put end game content here
print("Thank you for playing")