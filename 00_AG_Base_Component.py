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


def int_check(question, low=None, high=None, exit_code=None):
    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue

# Main routine does here
played_before = yes_no("Have you played the game before? ")
print()
if played_before == "no":
    instructions()

game_summary = []

rounds_played = 0
rounds_right = 0

rounds_wrong = 0

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

    num_1 = random.randint(0, 50)
    num_2 = random.randint(0, 50)

    print()
    print("What is {} + {} = ? ".format(num_1, num_2))

    total = num_1 + num_2

    # User input
    users_answer = int(input("Your answer: "))
    print()

    if users_answer == "xxx":
            rounds_played -= 1
            end_game = "yes"
            break

    # Check users answer

    if users_answer == total:
        print("Well done you got it right")
        rounds_right += 1
    else:
        print("Sorry you got it wrong. The correct answer was {}".format(total))
        rounds_wrong += 1

    choose = input("'xxx' to exit game or press enter to continue.... ")
    print()

    # End game if exit code is typed
    if choose == "xxx":
        break

    if users_answer == total:
        feedback = "Well done, you got it"
    else:
        feedback = "Sorry you got it wrong"

    # end game if requested # of rounds has been played

    outcome = "Question {}: {}".format(rounds_played + 1, feedback)

    # Outputs results...
    game_summary.append(outcome)
    print(feedback)

    rounds_played += 1 

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

rounds_won = rounds_played - rounds_wrong

print()
print('***** End Game Summary *****')
print("Right: {} \t|\t Wrong: {}".format(rounds_right, rounds_wrong))
print()

# Ask user if they want to see game summary

rounds = input("Please press <enter> to see your game summary.... ")

# **** Calculate Game Stats ******

print()
print("**** Game History *******")
for game in game_summary:
    print(game)

print()

# display game stats with $ values to the nearest whole number
print("******* Game Statistics ********")
print("Wrong: {} \nRight: {}".format(rounds_right, rounds_wrong))
