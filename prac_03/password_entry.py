"""Aivan"""

MIN_LENGTH = 4
#
# password = input("Please enter a password of at least {} characters: ".format(MIN_LENGTH))
# while len(password) < MIN_LENGTH:
#     password = input("Please enter a password of at least {} characters: ".format(MIN_LENGTH))
#
# print("*" * len(password))

def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(min_length):
    password = input("Please enter password of at least {} characters: ".format(min_length))
    while len(password) < min_length:
        print("Password is too short")
        password = input("Please enter password of at least {} characters: ".format(min_length))
    return password

def print_asterisks(sequence):
    print('*' * len(sequence))


main()