import random

NUMBERS_PER_QUICK_PICK = 6
MIN = 1
MAX = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Please enter a valid number!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for h in range(NUMBERS_PER_QUICK_PICK):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))

main()
