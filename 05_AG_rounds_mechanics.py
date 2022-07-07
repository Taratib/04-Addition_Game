import random


def check_rounds():
    while True:
        print()
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here

rounds_played = 0
choose_instruction = "What's the answer: "


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

    choose = input("{} ".format(choose_instruction))

    # End game if exit code is typed
    if choose == "xxx":
        break

    # **** rest of loop / game *****

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Put end game content here
print("Thank you for playing")
