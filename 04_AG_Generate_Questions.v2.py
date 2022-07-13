import random

for item in range(1, 4):
    num_1 = random.randint(1, 50)
    num_2 = random.randint(1, 50)

    print()
    print("What is {} + {} = ? ".format(num_1, num_2))

    total = num_1 + num_2

    users_answer = input("Answer question of 'xxx' to exit:")

    # End game if exit code is typed
    if users_answer == "xxx":
        break

    # Check users answer 

    if users_answer == total:
        print("Well done you got it right")
    else:
        print("Sorry you got it wrong. The correct answer was {}".format(total))
