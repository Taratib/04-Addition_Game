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
    print()
    print("**** How to Play ****")
    print()
    print('''Welcome to Addition Quiz this is how you play.
    
    - Choose how many questions you wnat or press <enter>
    for continuous mode.

    - Every question generates two random numbers for you to 
    figure out the answer.

    - If you wish to exit the quiz enter "xxx".

    - When you enter your answer it will tell you
    if you got it wrong or right.

    - When you finish all your questions your game summary is 
    shown at the end.

    Enjoy !!!!!!!''')
    print()

    return""


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


def check_questions():
    while True:
        response = input("How many question: ")

        round_error = "Please type either <enter> or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            # if response is not an integer go back to
            # start of loop

            except ValueError:
                print(round_error)
                continue

        return response


def int_check(question, users_answer=None, exit_code="xxx"):
    while True:

        # sets up error message
        if users_answer is None:
            error = "Please enter an integer"

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

questions_played = 0
questions_right = 0

questions_wrong = 0

# Ask user for # of rounds, <enter> for infinite mode
questions = check_questions()

end_game = "no"
while end_game == "no":

    # Start of the Game Play Loop

    # Rounds Heading
    print()
    if questions == "":
        heading = "Continuous Mode: Question {}".format(questions_played + 1)

    else:
        heading = "Question {} of {}".format(questions_played + 1, questions)

    print(heading)

    num_1 = random.randint(0, 50)
    num_2 = random.randint(0, 50)

    print()
    print("What is {} + {} = ? ".format(num_1, num_2))

    total = num_1 + num_2

    # User input
    users_answer = int_check("Your answer: ")
    print()

    # End game if exit code is typed
    if users_answer == "xxx":
        break

# Check users answer

    if users_answer == total:
        feedback = "Well done you got it right!"
        questions_right += 1
    else:
        feedback = "Sorry incorrect! Correct answer {}".format(total)
        questions_wrong += 1

    # end game if requested # of questions has been played

    outcome = "Question {}: {}".format(questions_played + 1, feedback)

    # Outputs results...
    game_summary.append(outcome)
    print(feedback)

    questions_played += 1

    # end game if requested # of questions has been played
    if questions_played == questions:
        break

questions_won = questions_played - questions_wrong

print()
print('***** End Game Summary *****')
print("Right: {} \t|\t Wrong: {}".format(questions_right, questions_wrong))
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
print("Wrong: {} \nRight: {}".format(questions_right, questions_wrong))