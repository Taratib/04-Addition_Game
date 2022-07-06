import random

for item in range(1, 4):
    num_1 = random.randint(1, 50)
    num_2 = random.randint(1, 50)

    print()
    print("What is {} + {} = ? ".format(num_1, num_2))

    total = num_1 + num_2

    # User input
    print()
    users_answer = int(input("Your answer: "))
    print()
    # Check users answer

    if users_answer == total:
        print("Well done you got it right")
    else:
        print("You got it incorrect. The correct answer was {}".format(total))
